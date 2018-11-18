from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/translation')
def trans():
    return render_template('translation.html')