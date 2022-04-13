# Libraries
import os
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# From Folders
from helpers.variables import  *

app= Flask(__name__)

# Connect Postgres database
app.config['SQLALCHEMY_DATABASE_URI']= POSTGRES_SQLALCHEMY_DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= POSTGRES_SQLACHEMY_TRACK_MODS
app.secret_key= POSTGRES_SECRET_KEY

db= SQLAlchemy(app)

# Retrieve the tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    response= requests.get(ZENDESK_TICKET_API, headers={'Authorization': 'Basic ' + ZENDESK_API_KEY })
    return response.json()

# Display information about the API calls
@app.route('/', methods=['GET'])
def hello():
    return POSTGRES_SQLALCHEMY_DB_URI

if __name__ == '__main__':
    app.run(host='0.0.0.0')