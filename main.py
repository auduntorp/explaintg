from flask import Flask, request

from describe_image import analyze

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/', methods=['POST'])
def hello_world():
    return str(analyze(request.data))

if __name__ == '__main__':
    app.run()
