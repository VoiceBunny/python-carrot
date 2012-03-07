# Python Carrot - VoiceBunny Library

[Python Carrot](https://github.com/Voice123/python-carrot) is a Python module that provides connection to the [VoiceBunny.com](http://voicebunny.com) HTTP RESTful API, using the library [Requests](https://github.com/kennethreitz/requests) for the HTTP request/response cycle.
If you need more information on how to use our module check the [installation guide](https://github.com/Voice123/python-carrot/wiki/installation) or the [tutorial](https://github.com/Voice123/python-carrot/wiki/Use-tutorial).

### Usage

```python
# Initialize the module
vb_carrot = PythonCarrot.VBCarrot('0','XXX')

# Get information
response = vb_carrot.gender_ages()
print response['genderandages']

# Post project
project={
    'script': "Test project",
    'specialInstructions': "Posted from Ruby-Carrot",
    'title' : "Test Project" 
}
response = vb_carrot.create_project(project)
print response['project']

# Get a project
response = vb_carrot.get_project(response['project']['id'])
print response['projects']
```

### Request a VoiceBunny API Key
To use this library you need to request an API Key in the [VoiceBunny.com Developer's Section](http://voicebunny.com/developers/token).

### Don't you like Python?
If you're not confortable with Python language, you can also check our other libraries

* [Ruby Carrot](https://github.com/Voice123/ruby-carrot)
* Groovy Carrot (Coming Soon)

Or why not, build your own library/module from scratch checking the [API documentation](http://voicebunny.com/developers/index).

### Copyright

Copyright (c) 2008 Torrenegra IP, LLC. Distributed under Creative Commons [CC-BY license](http://creativecommons.org/licenses/by/3.0/).