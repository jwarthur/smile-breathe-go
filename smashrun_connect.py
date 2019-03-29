#! /usr/bin/python

import requests

print("Hello World!")

# Create the authentication url

url = "https://secure.smashrun.com/oauth2/authenticate?client_id=client&scope=read_activity&response_type=token&state=basic&redirect_uri=http://yoursite.com/callback"

## use try/except to catch any connection or timeout errors.


try:
    call = requests.get(url)
    print("Succesful connection", url)
    print(call)

except requests.exceptions.RequestException as err:
    '''
    This except is going to catch instances where there is a connection error.
    Other possible requests exceptions: HTTPError, ConnectionError, Timeout
    '''
    print("Ooops: Something went wrong",err)


if call.status_code != 200: ## if not successful
    print("Something went wrong:", call.json()['error_description'])
else:
    print("Successful call! You're good to go")
