from flask import Flask

def getTheories(text):
    theories = dict()
    try:
        with open(text) as f:
            data = f.readlines()
    except:
        return 'File not found!'
    for line in data:
        if line.strip() == '':
            continue
        try:
            number = int(line)
            mode = 'key'
        except ValueError:
            if mode == 'key':
                key = line.strip()
                theories[key] = ''
                mode = 'value'
                cnt  = 0
            else:
                if cnt > 0:
                    theories[key] += '\n\n'
                theories[key] += line.strip()
                cnt = cnt + 1
    return theories

app = Flask(__name__)
text = getTheories('theories.txt')


app = Flask(__name__)

@app.route('/')
def hello_world():
  return str(text)

if __name__ == '__main__':
  app.run()
