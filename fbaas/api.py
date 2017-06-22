import json
from flask import Flask, request, Response
from .constants import VERSION

app = Flask(__name__)


def map_mod_value(value):
    if value == 3:
        return ('Fizz', '3')
    elif value == 5:
        return ('Buzz', '5')
    elif value == 15:
        return ('FizzBuzz', '3 or 5')
    else:
        return ('Unmapped', 0)


def make_headers(body):
    headers = {}
    headers['Server'] = 'FBAAS/{version}'.format(version=VERSION)
    headers['Content-Type'] = 'application/json'
    headers['Content-Length'] = len(body)
    return headers


def make_response(mod_value, value, bounds):
    name_str, div_by_str = map_mod_value(mod_value)

    if value not in bounds:
        response = json.dumps({'error': 'Out of bounds'}) + '\n'
        status = 400
        headers = make_headers(response)
        return Response(response, status, headers)

    # You could also say that a check and a response for unhandled mod_values
    # would be appropriate here, But that is not part of the requirements.
    if value % mod_value == 0:
        response = json.dumps(
            {
                'value': '{value}'.format(value=name_str)
            }
        ) + '\n'
        status = 200
        headers = make_headers(response)
        return Response(response, status, headers)
    else:
        response = json.dumps(
            {
                'error': 'Not divisible by {div_by_str}'.format(
                    div_by_str=div_by_str)
            }
        ) + '\n'
        status = 404
        headers = make_headers(response)
        return Response(response, status, headers)


@app.route('/fizz/<num>')
def fizz(num):
    return make_response(3, int(num), range(1, 500))


@app.route('/buzz/<num>')
def buzz(num):
    return make_response(5, int(num), range(1, 500))


@app.route('/fizzbuzz/<num>')
def fizzbuzz(num):
    return make_response(15, int(num), range(1, 1000))


@app.errorhandler(404)
def object_not_found(e):
    response = json.dumps({
            'message': 'The requested path was not found'
    }) + '\n'
    status = 404
    headers = make_headers(response)
    return Response(response, status, headers)
