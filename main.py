from flask import Flask, request

from describe_image import analyze
from parser import getTheories
from matcher import match

app = Flask(__name__)
text = getTheories('theories.txt')

@app.route('/')
def hello_world():
    print("get")
    return open('upload_photo.html', 'r').read()


@app.route('/', methods=['POST'])
def analyze_image():
    print("post")
    file = request.files['upload_file']
    keywords = analyze(file)
    return str(match(keywords, text))

if __name__ == '__main__':
    app.run()
