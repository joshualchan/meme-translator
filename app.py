from flask import Flask, request
from flask import render_template
import requests
import translation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/handleTranslate',methods=["POST"])
def trans():
    url = request.form['url']
    result = translate.translate(url)
    print(request.form['url'])
    return render_template('translation.html', result=result, img_url = url)

if __name__ =="__main__":
    app.run(debug=True)

