import json

import datetime

from logging import exception

from flask import Flask, request,Response,send_from_directory

import requests

import json

import mysec

import time

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def send_text_message(contact_number,msg):

 payload = json.dumps({

 "messaging_product": "whatsapp",

 "recipient_type": "individual",

 "to": f"{contact_number}",

 "type": "text",

 "text": {

 "preview_url": False,

 "body": f"{msg}"

 }

 })

 response = requests.request("POST", facebook_url, headers=facebokk_headers, 

data=payload)

 print('response',response)

# print('response',response.json())

def send_first_button_msg(contact_number):

 payload = json.dumps({

 "messaging_product": "whatsapp",

 "recipient_type": "individual",

 "to": f"{contact_number}",

 "type": "interactive",

 "interactive": {

 "type": "button",

 "body": {

 "text": "Hi, Welcome to Nandankanan Zoo park \nDo you want to 

book tickets?"

 },

 "action": {

 "buttons": [

 {

 "type": "reply",

 "reply": {

 "id": "yes",

 "title": "Yes"

 }

 },

 {

 "type": "reply",

 "reply": {

 "id": "no",

 "title": "No"

 }

 }

 ]

 }

 }

 })



 response = requests.request("POST", facebook_url, headers=facebokk_headers, 
data=payload)
 
@app.route('/webhook',methods=['GET','POST'])
def webhhook():
 if request.method == 'POST':
 json_data = request.get_json()
 try:
 json_data['entry'][0]['changes'][0]['value']['statuses']
 return Response(status = 200) 
 except :
 if json_data['object'] == "whatsapp_business_account" and 
json_data.get('entry')[0].get('changes')[0].get('value').get('contacts') is not 
None:
 print("Enter into data data ")
 pass
 else:
 return Response(status = 200) 
 msg_type = json_data['entry'][0]['changes'][0]['value']['messages'][0]
['type']
 
 if msg_type == "text":
 msg_text = json_data['entry'][0]['changes'][0]['value']['messages']
[0]['text']['body']
 if str.lower(msg_text) == "hi" or str.lower(msg_text) == "hello":
 msg = "Thanks for connect us !"
 send_text_message(contact_number,msg)
 return Response(status = 200) 
 return Response(status = 200) 
if __name__ == '__main__':
 app.run(host="0.0.0.0",port=5000,debug=True)
