from flask import Flask, request
from flask import render_template
#from transation import translate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/handleTranslate',methods=["POST"])
def trans():
    print(request.form['url'])
    return render_template('translation.html')

if __name__ =="__main__":
    app.run(debug = True)