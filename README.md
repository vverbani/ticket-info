# Ticket Info

Designed to retrieve Zendesk ticket information from an organization then store it in a SQL database using the Zendesk Ticket API. Once stored in the database, this information is pulled and displayed on the Dashboard where users can filter the data using a table UI.

## Additional Information About Zendesk

By default Zendesk API is protected by authentication. There's a couple of different methods for exposing this API however, user and password combination and basic authentication. For the purpose of not exposing our passwords we'll be using the (API authentication)[https://support.zendesk.com/hc/en-us/articles/4408889192858-Generating-a-new-API-token] token method.

After you generate your token, make this call in your terminal to base64 encode it:

```bash
echo -n {your_Zendesk_email/token:{api_token}} | openssl base64
```

The above is needed in order to use this project. In order for this project to use your token authentication, it passes this in the header as `Authorization: Basic {base64_email_token_combination}`.


## Getting Started

1. Clone this Repo
2. Head over to this directory
3. Create Zendesk API Key
4. `docker-compose up`
5. Visit http://localhost:{port} - where port is drawn from the docker-compose.yml file

### Tech Stack

1. Python: Retrieving the information
2. SQL: Storing the retrieved information
3. React/Next.js: Front end dashboard
4. Docker/Docker-compose: Containerize each service and ready it with `docker-compose up`