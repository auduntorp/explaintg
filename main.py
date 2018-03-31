from flask import Flask

#from describe_image import analyze
from parser import getTheories
#from matcher import match

app = Flask(__name__)
text = getTheories('theories.txt')


app = Flask(__name__)

@app.route('/')
def hello_world():
  return str(text)

if __name__ == '__main__':
  app.run()
