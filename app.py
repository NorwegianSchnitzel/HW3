from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle = 'My Calculator')

@app.route('/Eric')
def eric():
    return render_template('eric.html', pageTitle = 'Erics page')


if __name__ == '__main__':
    app.run(debug=True)