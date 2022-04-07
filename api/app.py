import os
import requests
from dotenv import load_dotenv, find_dotenv
from flask import Flask

app = Flask(__name__)

# Locate .env file in your directory
load_dotenv(find_dotenv())

# Retrieve the tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    response = requests.get(os.environ.get("ZENDESK_TICKET_API"), headers={'Authorization': 'Basic ' + os.environ.get("API_KEY") })
    return response.json()

# Display information about the API calls
@app.route('/', methods=['GET'])
def hello():
    return 'Welcome to the Open-Source Ticket Info Project'

if __name__ == '__main__':
    app.run(host='0.0.0.0')