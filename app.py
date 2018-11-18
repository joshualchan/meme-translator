from flask import Flask, request
from flask import render_template
import requests
# import translation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/handleTranslate',methods=["POST"])
def trans():
    url = request.form['url']
    result = translate(url)
    print(request.form['url'])
    return render_template('translation.html', result=result)

if __name__ =="__main__":
    app.run(debug=True)

import json

#meme_url = input()

#https://qph.fs.quoracdn.net/main-qimg-71c13b45494b4c0408a8eb164aedacb6-c

def translate(meme_url):
    url = "https://vision.googleapis.com/v1/images:annotate"

    querystring = {"key":"AIzaSyDRDkVOoM0lwfFB9Za_Q64RquAbqBrPEiI"}

    payload = "{\"requests\": [  { \"image\": {  \"source\": {    \"imageUri\": \"" + meme_url + "\" }  },  \"features\": [ { \"type\": \"TEXT_DETECTION\"  } ] }  ]}"
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "1e05ec6e-cced-4d13-ae85-34509aa0c198"
        }




    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    r1 = json.loads(response.text)
    description = r1['responses'][0]['textAnnotations'][0]['description']
    language = r1['responses'][0]['textAnnotations'][0]['locale']
    #print(description)


    response2= requests.get("https://translation.googleapis.com/language/translate/v2?key=AIzaSyDRDkVOoM0lwfFB9Za_Q64RquAbqBrPEiI&q="+description+"&target=en&source=" + language).text

    jres = json.loads(response2)

    eng_translation = jres['data']['translations'][0]['translatedText']
    return description + eng_translation


#print(translate(meme_url))
