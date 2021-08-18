import unittest
import http
import json

from flask import Flask
from app import app
# set our application to testing mode
app.testing = True

class Test_app(unittest.TestCase):

    def test_helloworld(self):        
        with app.test_client() as client:

            #get hello world response
            result = client.get('/')

            # check result from server with expected data
            self.assertEqual(
                json.loads(result.data),
                { "message" : "hello world!"}
            )

if __name__ == '__main__':
    unittest.main()