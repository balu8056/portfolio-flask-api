from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.get('/')
def home():
    return {'greet': 'welcome'}


@app.get('/hello/greet')
def home():
    return {'greet': 'welcome Bala!'}


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
