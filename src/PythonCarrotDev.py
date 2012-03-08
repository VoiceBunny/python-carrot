"""
Author::    Jorge Vargas  (mailto:jorge.vargas@voicebunny.com)
Copyright:: Copyright (c) 2008 Torrenegra IP, LLC.
License::   Distributed under Creative Commons CC-BY license http://creativecommons.org/licenses/by/3.0/
"""

# Filename: PythonCarrotDev.py
import requests
import simplejson
from requests.auth import HTTPBasicAuth

class VBCarrot:

    def say_hi():
        print 'Hi, folks!'


    # http://127.0.0.1:8080/test URL for test with mocks
    # https://api.local.voicebunny.com Local enviroment
    def __init__(self, api_id, api_key, url):
        self.api_id = api_id
        self.api_key = api_key
        self.url = url

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
        req = requests.post(self.url+'/projects/add.json',
            project, 
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def force_dispose(self, project_id):
        req = requests.get(self.url+'/projects/forceDispose/'+str(project_id)+'.json',
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def quote(self, text, contest=0, maxEntries=3):
        req = requests.post(self.url+'/projects/quote.json', 
            data={
                'script': text,
                'contest': contest,
                'maxContestEntries': maxEntries
            },
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


version = '0.6.5'

# End of PythonCarrotDev.py