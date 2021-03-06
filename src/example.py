"""
Author::    Jorge Vargas  (mailto:jorge.vargas@voicebunny.com)
Copyright:: Copyright (c) 2008 Torrenegra IP, LLC.
License::   Distributed under Creative Commons CC-BY license http://creativecommons.org/licenses/by/3.0/
"""

import PythonCarrotDev
import requests
import simplejson
from requests.auth import HTTPBasicAuth

vb_carrot = PythonCarrot.VBCarrot('xx','xxxxXXXXxxxxXXXX')

balance = vb_carrot.balance()
print "Your account balance is: "+ balance['balance']['amount'] +" "+ balance['balance']['currency']
current_balance = float(balance['balance']['amount'])

#script = '{"part001": "Hi", "part002": "World", "part003": "Bye, I have to go"}'
script = {
    "part001":"Hi",
    "part002":"World",
    "part003":"Bye, I have to go"
}

language = "eng-us"

quoteData = {
    "script": script,
    "language": language
}

quote = vb_carrot.quote(quoteData)
price = str(quote['quote']['price'])
print "Posting this script will cost: "+ price +" "+ quote['quote']['currency']
reward = float(quote['quote']['price'])

if current_balance >= reward:
    # Remember to send the script argument always as a json string when using multiparts
    project = {
        'title': 'project posted from Python Carrot',
        'script': simplejson.dumps(script),
        'remarks': "I want the voice be similar to Bugs Bunny.",
        'price':reward,
        'test': '1'
    }
    response = vb_carrot.create_project(project)
    if 'error' in response:
        print "Something happened: "+ response['error']['message']
    else:
        print "Project ID:"+response['project']['id']+" successfully posted."
else:
    print "You dont have enough money to post this project."

raw_input()