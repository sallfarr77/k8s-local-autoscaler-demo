from flask import Flask, render_template_string
import os
import socket
import subprocess

app = Flask(__name__)

# Function to check if HPA & VPA are enabled
def check_autoscaling():
    try:
        hpa_status = subprocess.run(["kubectl", "get", "hpa"], capture_output=True, text=True)
        vpa_status = subprocess.run(["kubectl", "get", "vpa"], capture_output=True, text=True)
        hpa_enabled = "NAME" in hpa_status.stdout and len(hpa_status.stdout.splitlines()) > 1
        vpa_enabled = "NAME" in vpa_status.stdout and len(vpa_status.stdout.splitlines()) > 1
        if hpa_enabled and vpa_enabled:
            return "Enabled (HPA & VPA)"
        elif hpa_enabled:
            return "Enabled (HPA Only)"
        elif vpa_enabled:
            return "Enabled (VPA Only)"
        else:
            return "Disabled"
    except Exception as e:
        print(f'Error fetching autoscaling status: {e}')
        return "Autoscaling status unavailable"
        return "Error fetching autoscaling status"

@app.route('/')
def hello():
    pod_name = os.getenv("POD_NAME") or socket.gethostname()
    pod_ip = socket.gethostbyname(socket.gethostname())
    autoscaling_status = check_autoscaling()
    
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kubernetes Autoscaler Demo</title>
        <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path fill='%23007bff' d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z'/></svg>">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap');
            body {
                font-family: 'Poppins', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                text-align: center;
            }
            .container {
                background: rgba(255, 255, 255, 0.2);
                padding: 50px;
                border-radius: 20px;
                backdrop-filter: blur(12px);
                box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .container:hover {
                transform: translateY(-10px);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            }
            h1 {
                font-size: 2.8em;
                margin-bottom: 25px;
                font-weight: 700;
            }
            p {
                font-size: 1.3em;
                margin-bottom: 15px;
                font-weight: 400;
            }
            img {
                width: 140px;
                margin-bottom: 25px;
            }
            button {
                padding: 15px 35px;
                font-size: 20px;
                font-weight: 600;
                color: white;
                background-color: #ff9800;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }
            button:hover {
                background-color: #e68900;
                transform: scale(1.08);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg" alt="Kubernetes Logo">
            <h1>Kubernetes Autoscaler Demo</h1>
            <p>This application is running on:</p>
            <p><strong>Pod Name:</strong> {{ pod_name }}</p>
            <p><strong>Pod IP:</strong> {{ pod_ip }}</p>
            <p><strong>Autoscaling:</strong> {{ autoscaling_status }}</p>
            <button onclick="alert('Scaling with Kubernetes is powerful!')">Try Scaling</button>
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(html_content, pod_name=pod_name, pod_ip=pod_ip, autoscaling_status=autoscaling_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
