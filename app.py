from unittest import result
from flask import Flask, request, make_response
from dbhelpers import run_statement
from apihelpers import check_endpoint_info
from dbcreds import production_mode
import json

app = Flask(__name__)

@app.post('/api/artist')
def add_artist():
    is_valid = check_endpoint_info(request.json, ['artist', 'date_painted', 'image_url', 'name'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL insert_artist(?,?,?,?)',
    [request.json.get('artist'), request.json.get('date_painted'), request.json.get('image_url'), request.json.get('name')])

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Sorry, an error has occured.', default=str), 500)

@app.get('/api/artist')
def get_artist():
    is_valid = check_endpoint_info(request.args, ['artist'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL get_artist(?)', [request.args.get('artist')])

    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps("Sorry, an error have occured."), 500)

if(production_mode):
    print("Running in Production Mode")
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)