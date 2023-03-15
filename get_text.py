from flask import Flask

app = Flask(__name__)

@app.route('')
def get_text():
    with open('get_text.py', 'r') as f:
        text = f.read()
    return text

if __name__ == '__main__':
    app.run()