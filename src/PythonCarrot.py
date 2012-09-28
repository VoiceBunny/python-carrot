"""
Author::    Jorge Vargas  (mailto:jorge.vargas@voicebunny.com)
Copyright:: Copyright (c) 2008 Torrenegra IP, LLC.
License::   Distributed under Creative Commons CC-BY license http://creativecommons.org/licenses/by/3.0/
"""

# Filename: PythonCarrot.py
import requests
import simplejson
from requests.auth import HTTPBasicAuth

class VBCarrot:

    def say_hi():
        print 'Hi, this is the python carrot.'

    def __init__(self, api_id, api_key, dev=False):
        self.api_id = api_id
        self.api_key = api_key
        self.url = 'https://api.voicebunny.com'

    def languages(self):
        req = requests.get(self.url+'/languages.json',
            verify=False)
        data = simplejson.loads(req.text)
        return data

    def gender_ages(self):
        req = requests.get(self.url+'/genderAndAges.json',
            verify=False)
        data = simplejson.loads(req.text)
        return data

    def balance(self):
        req = requests.get(self.url+'/balance.json',
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def all_projects(self):
        req = requests.get(self.url+'/projects.json',
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def get_project(self, project_id):
        req = requests.get(self.url+'/projects/'+str(project_id)+'.json',
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def create_project(self, project):
        print project
        req = requests.post(self.url+'/projects/addSpeedy.json',
            data=project, 
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def create_booking_project(self, project):
        req = requests.post(self.url+'/projects/addBooking.json',
            project, 
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def force_dispose(self, project_id):
        req = requests.get(self.url+'/projects/forceDispose/'+str(project_id)+'.json',
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def quote(self, params):
        req = requests.post(self.url+'/projects/quote.json', 
            params,
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def get_read(self, read_id):
        req = requests.get(self.url+'/reads/'+str(read_id)+'.json',
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def approve_read(self, read_id):
        req = requests.get(self.url+'/reads/approve/'+str(read_id)+'.json',
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def reject_read(self, read_id):
        req = requests.get(self.url+'/reads/reject/'+str(read_id)+'.json',
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data


version = '0.7.1'

# End of PythonCarrot.py