"""
Author::    Jorge Vargas  (mailto:jorge.vargas@voicebunny.com)
Copyright:: Copyright (c) 2008 Torrenegra IP, LLC.
License::   Distributed under Creative Commons CC-BY license http://creativecommons.org/licenses/by/3.0/
"""

import PythonCarrotDev

import requests
import simplejson
from requests.auth import HTTPBasicAuth

vb_carrot = PythonCarrotDev.VBCarrot('85','de52c722a40ea875ce89ae134a9ad66071144f5e', 'https://api.local.voicebunny.com')
response = vb_carrot.gender_ages()
print response['genderandages']

project={
    'script': "Test project",
    'specialInstructions': "Posted from Ruby-Carrot",
    'title' : "Test Project" 
}
response = vb_carrot.create_project(project)
print response['project']

response = vb_carrot.get_project(response['project']['id'])
print response['projects']


raw_input()