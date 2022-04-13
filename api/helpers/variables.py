import os
from dotenv import load_dotenv, find_dotenv

# Locate .env file in your directory
load_dotenv(find_dotenv())

# Set variables from .env file
POSTGRES_USER= os.environ.get("POSTGRES_USER")
POSTGRES_DB= os.environ.get("POSTGRES_DB")
POSTGRES_PASSWORD= os.environ.get("POSTGRES_PASSWORD")
POSTGRES_SECRET_KEY= os.environ.get("POSTGRES_SECRET_KEY")
POSTGRES_SQLACHEMY_TRACK_MODS= False
POSTGRES_SQLALCHEMY_DB_URI= os.environ.get("POSTGRES_SQLALCHEMY_DB_URI")

ZENDESK_API_KEY= os.environ.get("API_KEY")
ZENDESK_TICKET_API= os.environ.get("ZENDESK_TICKET_API")

