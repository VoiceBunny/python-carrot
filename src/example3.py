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

wordsToChange = 5
readId = 75
voiceBunnyError = 1
instructions = 'Please correct the 4th word.'

quoteParams = {
    'wordsAddedOrChanged': wordsToChange,
    'voiceBunnyError': voiceBunnyError

}

quote = vb_carrot.revision_quote(readId, quoteParams)
price = str(quote['quote']['price'])
print "Posting this revision will cost: "+ price +" "+ quote['quote']['currency']
reward = float(quote['quote']['price'])

revision = {
    'wordsAddedOrChanged': wordsToChange,
    'voiceBunnyError': voiceBunnyError,
    'instructions': instructions
}
response = vb_carrot.revision_add(readId, revision)
if 'error' in response:
    print "Something happened: "+ response['error']['message']
else:
    print "Revision ID:"+response['project']['id']+" successfully posted."

raw_input()