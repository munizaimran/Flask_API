from flask import Flask, render_template, request, jsonify
from flask import send_from_directory

import os,sys,requests, json
from random import randint

app = Flask(__name__, template_folder='web')

@app.route('/web/')
def render_page_web():
    return render_template('index.html')

@app.route('/parse',methods=['POST', 'GET'] )
def extract():
  text=str(request.form.get('value1'))
  payload = json.dumps({"sender": "Rasa","message": text})
  headers = {'Content-type': 'application/json', 'Accept':     'text/plain'}
  response = requests.request("POST",   url="http://localhost:5005/webhooks/rest/webhook", headers=headers, data=payload)
  response=response.json()
  resp=[]
  for i in range(len(response)):
    try:
      resp.append(response[i]['text'])
    except:
      continue
  result=resp
  return render_template('index.html', result=result,text=text)
if __name__ == "__main__":
  app.run(debug=True)