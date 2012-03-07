"""
Author::    Jorge Vargas  (mailto:jorge.vargas@voicebunny.com)
Copyright:: Copyright (c) 2008 Torrenegra IP, LLC.
License::   Distributed under Creative Commons CC-BY license http://creativecommons.org/licenses/by/3.0/
"""

import unittest
import PythonCarrot

class TestPythonCarrot(unittest.TestCase):

    def setUp(self):
        self.pc= PythonCarrot.VBCarrot('1','XXXX', True)

    def test_balance(self):
        response = self.pc.balance()
        self.assertEqual(response['balance']['amount'], '1000.98')
        self.assertEqual(response['balance']['currency'], 'usd')

    def test_all_projects(self):
        response = self.pc.all_projects()
        self.assertEqual(response['projects'][1]['id'],'2')
        self.assertEqual(response['projects'][1]['language'],'eng-us' )
        self.assertEqual(response['projects'][1]['rewardCurrency'],'usd')

    def test_get_project(self):
        response = self.pc.get_project(1)
        self.assertEqual(response['projects'][0]['id'],'1' )
        self.assertEqual(response['projects'][0]['language'], 'eng-us')
        self.assertEqual(response['projects'][0]['rewardCurrency'],'usd')

    def test_create_project(self):
        project={
            'title': 'Testing the API',
            'script': 'The quick brown fox jumps over the lazy dog',
            'rewardAmount': 1,
            'rewardcurrency': 'usd',
            'language': 'eng-us',
            'genderAndAge': 'baby',
            'lifetime': 86400,
            'specialinstructions': 'None'
        }
        response = self.pc.create_project(project)
        self.assertEqual(response['project']['id'],'2')
        self.assertEqual(response['project']['language'],'eng-us')
        self.assertEqual(response['project']['rewardCurrency'],'usd')

    def test_get_project(self):
        response = self.pc.get_project(1)
        self.assertEqual(response['projects'][0]['id'],'1')
        self.assertEqual(response['projects'][0]['language'],'eng-us')
        self.assertEqual(response['projects'][0]['rewardCurrency'],'usd')

    
    def test_force_dispose(self):
        response = self.pc.force_dispose(1)
        self.assertEqual(response['projects'][0]['id'],'1')
        self.assertEqual(response['projects'][0]['language'],'eng-us')
        self.assertEqual(response['projects'][0]['rewardCurrency'],'usd')

    def test_quote(self):
        response = self.pc.quote(" ")
        self.assertEqual(response['quote']['rewardAmount'],'0')
        self.assertEqual( response['quote']['rewardCurrency'],'usd')

    def test_get_read(self):
        response = self.pc.get_read(1)
        self.assertEqual(response['reads'][0]['id'],'1')
        self.assertEqual(response['reads'][0]['user'],'0')
        self.assertEqual(response['reads'][0]['project'],'2')

    def test_approve_read(self):
        response = self.pc.approve_read(1)
        self.assertEqual( response['reads'][0]['id'],'1')
        self.assertEqual(response['reads'][0]['user'],'0')
        self.assertEqual(response['reads'][0]['project'],'2')

    def test_reject_read(self):
        response = self.pc.reject_read(1)
        self.assertEqual( response['reads'][0]['id'],'1')
        self.assertEqual(response['reads'][0]['user'],'0')
        self.assertEqual(response['reads'][0]['project'],'2')

    def test_languages(self):
        response = self.pc.languages()
        self.assertEqual(response['languages'][0]['id'],'ara')
        self.assertEqual(response['languages'][1]['id'],'ben')
        self.assertEqual(response['languages'][2]['id'],'bos-ba')

    def test_gender_ages(self):
        response = self.pc.gender_ages()
        self.assertEqual(response['genderandages'][0]['code'],'baby')
        self.assertEqual( response['genderandages'][1]['code'],'child')
        self.assertEqual(response['genderandages'][2]['code'],'teenageGirl')


if __name__ == '__main__':
    unittest.main()