from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/Eric')
def eric():
    return "Hello, it's Eric"


if __name__ == '__main__':
    app.run(debug=True)