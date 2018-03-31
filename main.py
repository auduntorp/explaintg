from flask import Flask, request

from describe_image import analyze

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("get")
    return open('upload_photo.html', 'r').read()


@app.route('/', methods=['POST'])
def analyze_image():
    print("post")
    file = request.files['upload_file']
    print(file)
    return str(analyze(file))

if __name__ == '__main__':
    app.run()
