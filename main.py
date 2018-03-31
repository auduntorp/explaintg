from flask import Flask, request, render_template

from describe_image import analyze
from parser import getTheories
from matcher import match

app = Flask(__name__)
text = getTheories('theories.txt')

@app.route('/', methods=['GET'])
def hello_world():
    print("get")
    #return open('upload_photo.html', 'r').read()
    return render_template('index.html')


@app.route('/', methods=['POST'])
def analyze_image():
    print("post woo12")
    #filename = request.form['file']
    #print(filename)
    print(request.files)
    file = request.files['file']
    print(file)
    print('analyzing')
    keywords = analyze(file)
    print('matching')
    
    print(str(match(keywords, text)))
    return "Hello world!"

if __name__ == '__main__':
    app.run()
