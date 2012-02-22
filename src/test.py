#------ imports ----
import PythonCarrot


import requests
import simplejson
from requests.auth import HTTPBasicAuth


#r = requests.get('https://api.voicebunny.com/languages', auth=HTTPBasicAuth('1', '478c35ec24ff7621c1b2e932d367a41a'),verify=False)
#print r.headers['content-type']
#print r.status_code
#print r.content
#data = simplejson.loads(r.text)
#print data['languages']


#PythonCarrot.sayhi()
#print 'Version', PythonCarrot.version


#------- Languages ---------------
"""

url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
req = requests.get(url+'/languages',
    verify=False)
data = simplejson.loads(req.text)
response = data['languages']


#------- Gender And Ages ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
req = requests.get(url+'/genderAndAges',
    verify=False)
data = simplejson.loads(req.text)
response = data['genderandages']


#------- Balance ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
req = requests.get(url+'/balance',
    auth=HTTPBasicAuth(api_id, api_key),verify=False)
data = simplejson.loads(req.text)
response = data['balance']

#------- GET Projects ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
req = requests.get(url+'/projects',
    auth=HTTPBasicAuth(api_id, api_key),verify=False)
data = simplejson.loads(req.text)
response = data['projects']


#------- GET Project ID ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
project_id = '25'
req = requests.get(url+'/projects/'+project_id,
   auth=HTTPBasicAuth(api_id, api_key),verify=False)
data = simplejson.loads(req.text)
response = data['projects']

#------- Quote Text ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
req = requests.get(url+'/projects/quote', 
    data={'text': 'Script sample'},
    auth=HTTPBasicAuth(api_id, api_key),verify=False)
data = simplejson.loads(req.text)
response = data['quote']

#------- GET READ ID ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
read_id = '35'
req = requests.get(url+'/reads/'+read_id,
    auth=HTTPBasicAuth(api_id, api_key),verify=False)
data = simplejson.loads(req.text)
response = data['reads']

#------- APPROVE READ ID ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
read_id = '35'
req = requests.get(url+'/reads/approve/'+read_id,
    auth=HTTPBasicAuth(api_id, api_key),verify=False)
data = simplejson.loads(req.text)
response = data['reads']

#------- REJECT READ ID ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
read_id = '35'
req = requests.get(url+'/reads/reject/'+read_id,
    auth=HTTPBasicAuth(api_id, api_key),verify=False)
data = simplejson.loads(req.text)
response = data['reads']

#------- Dispose Project ID ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
project_id = '25'
req = requests.get(url+'/projects/forceDispose/'+project_id,
    auth=HTTPBasicAuth(api_id, api_key),verify=False)
data = simplejson.loads(req.text)
response = data['projects']

#------- Quote Text ---------------
url = 'https://api.dev.voicebunny.com'
api_id = '85'
api_key = 'de52c722a40ea875ce89ae134a9ad66071144f5e'
req = requests.post(url+'/projects/add',
   data={
        'title': 'Testing the API',
        'script': 'The quick brown fox jumps over the lazy dog',
        'rewardAmount': '1',
        'rewardcurrency': 'usd',
        'language': 'eng-us',
        'genderAndAge': 'baby',
        'lifetime': '86400',
        'specialinstructions': 'None'
   }, 
   auth=HTTPBasicAuth(api_id, api_key),verify=False)
data = simplejson.loads(req.text)
response = data['project']


#------- Output -----------
"""
pc= PythonCarrot.VBCarrot('85','de52c722a40ea875ce89ae134a9ad66071144f5e')

#data = pc.languages()
#data = pc.gender_ages()
#data = pc.balance()
#data = pc.all_projects()
#data = pc.get_project(25)
#project={
#    'title': 'Testing the API',
#    'script': 'The quick brown fox jumps over the lazy dog',
#    'rewardAmount': 1,
#    'rewardcurrency': 'usd',
#    'language': 'eng-us',
#    'genderAndAge': 'baby',
#    'lifetime': 86400,
#    'specialinstructions': 'None'
#}
#data = pc.create_project(project)
#data = pc.force_dispose(25)
#data = pc.quote('Hola mundo sa dsa dasdssa dsad sasdasdsad!!!!')
data = pc.get_read(35)
#data = pc.approve_read(35)
#data = pc.reject_read(35)


print data;
raw_input()