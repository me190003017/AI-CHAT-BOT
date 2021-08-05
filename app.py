'''from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__, static_url_path='/static')

# a route to display our html page gotten from [react-chat-widget](https://github.com/mrbot-ai/rasa-webchat)
@app.route("/")
def index():
    return render_template('index.html')

# run the application
if __name__ == "__main__":
    app.run(debug=True)'''

from flask import Flask, redirect, url_for, request, render_template
import requests
import json
from bs4 import BeautifulSoup
import re

app = Flask(__name__, template_folder = 'templates2')
context_set = ""

@app.route('/', methods = ['POST', 'GET'])
def index():

	# if request.method == 'GET':
  	# 	val = str(request.args.get('text'))
  	# 	data = json.dumps({"sender": "Rasa","message": val})
  	# 	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  	# 	res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
  	# 	res = res.json()
  	# 	val = res[0]['text']
  	return render_template('index.html')

  #!/usr/bin/env python
# coding: utf-8


if __name__ == '__main__':
  app.run(debug=True)
