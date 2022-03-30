# Ticket Info

Designed to retrieve Zendesk ticket information from an organization then store it in a SQL database using the Zendesk Ticket API. Once stored in the database, this information is pulled and displayed on the Dashboard where users can filter the data using a table UI.

## Zendesk Information

By default Zendesk API is protected by authentication. There's a couple of different methods for exposing this API however, user and password combination and basic authentication. For the purpose of not exposing our passwords we'll be using the [API authentication](https://support.zendesk.com/hc/en-us/articles/4408889192858-Generating-a-new-API-token) token method.

After you generate your token, make this call in your terminal to base64 encode it:

```
echo -n {your_Zendesk_email/token:{api_token}} | openssl base64
```

The above is needed in order to use this project. In order for this project to use your token authentication, it passes this in the header as `Authorization: Basic {base64_email_token_combination}`.

## Getting Started

1. Clone this Repo
2. Head over to this directory
3. Create Zendesk API Key
4. Base64 encode the key
5. Upload it to the `.env` file under `API_KEY`
6. `docker-compose up`
7. Visit http://localhost:8000

### Tech Stack

1. Python: Retrieving the information
2. SQL: Storing the retrieved information
3. React/Next.js: Front end dashboard
4. Docker/Docker-compose: Containerize each service and ready it with `docker-compose up`

### Additional Information

Run the below command anytime you make an update to `requirements.txt`. It needs to be re-build to download all dependencies for the project:

```
docker-compose build
```

*** Ticket Info repository is not meant for production use as there's no form of security implemented for this. This is meant to be used locally for read only Zendesk ticket data. So please use at your own risk. Some precautionary changes are outlined with the `TO-DO` comment in the correct files. ***