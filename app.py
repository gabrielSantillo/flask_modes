from flask import Flask, request, make_response
from dbhelpers import run_statement
from apihelpers import check_endpoint_info
import json

app = Flask(__name__)



app.run(debug=True)