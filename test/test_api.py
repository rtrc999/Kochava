import sys
import os
import json
import unittest

from fbaas import app
from fbaas.api import map_mod_value
from fbaas.api import make_headers
from fbaas.constants import VERSION


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_map_mod_value(self):
        name, div_str = map_mod_value(3)
        self.assertEqual(name, 'Fizz')
        self.assertEqual(div_str, '3')

        name, div_str = map_mod_value(5)
        self.assertEqual(name, 'Buzz')
        self.assertEqual(div_str, '5')

        name, div_str = map_mod_value(15)
        self.assertEqual(name, 'FizzBuzz')
        self.assertEqual(div_str, '3 or 5')

    def test_make_headers(self):
        headers = make_headers('hello world')
        self.assertEqual(headers['Server'], 'FBAAS/{v}'.format(v=VERSION))
        self.assertEqual(headers['Content-Type'], 'application/json')
        self.assertEqual(headers['Content-Length'], 11)

    #
    # Testing Fizz
    #
    def test_fizz_response_ok(self):
        response = self.app.get('/fizz/3')
        self.assertEqual(response.status_code, 200)
        body = json.loads(response.data)
        self.assertEqual(body['value'], 'Fizz')

    def test_fizz_response_out_of_bounds(self):
        response = self.app.get('/fizz/0')
        self.assertEqual(response.status_code, 400)
        body = json.loads(response.data)
        self.assertEqual(body['error'], 'Out of bounds')

        response = self.app.get('/fizz/501')
        self.assertEqual(response.status_code, 400)
        body = json.loads(response.data)
        self.assertEqual(body['error'], 'Out of bounds')

    def test_fizz_response_not_ok(self):
        response = self.app.get('/fizz/5')
        self.assertEqual(response.status_code, 404)
        body = json.loads(response.data)
        self.assertEqual(body['error'], 'Not divisible by 3')

    #
    # Testing Buzz
    #
    def test_buzz_response_ok(self):
        response = self.app.get('/buzz/5')
        self.assertEqual(response.status_code, 200)
        body = json.loads(response.data)
        self.assertEqual(body['value'], 'Buzz')

    def test_buzz_response_out_of_bounds(self):
        response = self.app.get('/buzz/0')
        self.assertEqual(response.status_code, 400)
        body = json.loads(response.data)
        self.assertEqual(body['error'], 'Out of bounds')

        response = self.app.get('/buzz/501')
        self.assertEqual(response.status_code, 400)
        body = json.loads(response.data)
        self.assertEqual(body['error'], 'Out of bounds')

    def test_buzz_response_not_ok(self):
        response = self.app.get('/buzz/6')
        self.assertEqual(response.status_code, 404)
        body = json.loads(response.data)
        self.assertEqual(body['error'], 'Not divisible by 5')

    #
    # Testing FizzBuzz
    #
    def test_fizzbuzz_response_ok(self):
        response = self.app.get('/fizzbuzz/15')
        self.assertEqual(response.status_code, 200)
        body = json.loads(response.data)
        self.assertEqual(body['value'], 'FizzBuzz')

    def test_fizzbuzz_response_out_of_bounds(self):
        response = self.app.get('/fizzbuzz/0')
        self.assertEqual(response.status_code, 400)
        body = json.loads(response.data)
        self.assertEqual(body['error'], 'Out of bounds')

        response = self.app.get('/fizzbuzz/1001')
        self.assertEqual(response.status_code, 400)
        body = json.loads(response.data)
        self.assertEqual(body['error'], 'Out of bounds')

    def test_fizzbuzz_response_not_ok(self):
        response = self.app.get('/fizzbuzz/16')
        self.assertEqual(response.status_code, 404)
        body = json.loads(response.data)
        self.assertEqual(body['error'], 'Not divisible by 3 or 5')
