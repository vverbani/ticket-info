import os
import requests
from dotenv import load_dotenv, find_dotenv
from flask import Flask

app= Flask(__name__)

# Locate .env file in your directory
load_dotenv(find_dotenv())

# Set variables that we'll need
POSTGRES_USER= os.environ.get("POSTGRES_USER")
POSTGRES_DB= os.environ.get("POSTGRES_DB")
POSTGRES_PASSWORD= os.environ.get("POSTGRES_PASSWORD")
POSTGRES_SECRET_KEY= os.environ.get("POSTGRES_SECRET_KEY")
ZENDESK_API_KEY= os.environ.get("API_KEY")
ZENDESK_TICKET_API= os.environ.get("ZENDESK_TICKET_API")

# Connect Postgres database for data storing
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD + '@localhost/' + POSTGRES_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

# Retrieve the tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    response = requests.get(ZENDESK_TICKET_API, headers={'Authorization': 'Basic ' + ZENDESK_API_KEY })
    return response.json()

# Display information about the API calls
@app.route('/', methods=['GET'])
def hello():
    return 'Welcome to the Open-Source Ticket Info Project'

if __name__ == '__main__':
    app.run(host='0.0.0.0')