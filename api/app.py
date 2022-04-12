# Libraries
import os
import requests
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# From Folders
from helpers.variables import  *

app= Flask(__name__)

# Locate .env file in your directory
load_dotenv(find_dotenv())

# Set variables from .env file
POSTGRES_USER= os.environ.get("POSTGRES_USER")
POSTGRES_DB= os.environ.get("POSTGRES_DB")
POSTGRES_PASSWORD= os.environ.get("POSTGRES_PASSWORD")
POSTGRES_SECRET_KEY= os.environ.get("POSTGRES_SECRET_KEY")
ZENDESK_API_KEY= os.environ.get("API_KEY")
ZENDESK_TICKET_API= os.environ.get("ZENDESK_TICKET_API")

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
    print('=========================================')
    print(POSTGRES_SQLALCHEMY_DB_URI)
    return POSTGRES_SQLALCHEMY_DB_URI

if __name__ == '__main__':
    app.run(host='0.0.0.0')