"""
Author::    Jorge Vargas  (mailto:jorge.vargas@voicebunny.com)
Copyright:: Copyright (c) 2008 Torrenegra IP, LLC.
License::   Distributed under Creative Commons CC-BY license http://creativecommons.org/licenses/by/3.0/
"""

import PythonCarrotDev
import requests
import simplejson
from requests.auth import HTTPBasicAuth

vb_carrot = PythonCarrotDev.VBCarrot('xx','xxxxXXXXxxxxXXXX')

balance = vb_carrot.balance()
print "Your account balance is: "+ balance['balance']['amount'] +" "+ balance['balance']['currency']
current_balance = float(balance['balance']['amount'])

script = "What's up , folks?"
quote = vb_carrot.quote(script)
print "Posting this script will cost: "+ quote['quote']['rewardAmount'] +" "+ quote['quote']['rewardCurrency']
reward = float(quote['quote']['rewardAmount'])

if current_balance >= reward:
    project = {
        'script': script,
        'specialInstructions': "I want the voice be similar to Bugs Bunny.",
        'rewardAmount':reward,
        'rewardCurrency': 'usd',
        'test': '1'
    }
    vb_carrot.create_project(project)
    print "Project successfully posted."
else:
    print "You dont have enough money to post this project."

raw_input()