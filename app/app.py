from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello Kubernetes</title>
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            }
            .container {
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease;
            }
            .container:hover {
                transform: translateY(-10px);
            }
            h1 {
                color: #333;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            button {
                padding: 15px 30px;
                font-size: 18px;
                color: white;
                background-color: #007bff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }
            button:hover {
                background-color: #0056b3;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, Kubernetes!</h1>
            <button onclick="alert('Welcome to Kubernetes!')">Click Me</button>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)