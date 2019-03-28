#! /usr/bin/python

import requests
#from tokens import * ## loading our API details. Best to keep your credentials seperate so it's easier to manage when sharing your scripts


print("Hello World!")

## FYI - here's the search parameters we can use in our query
# https://www.eventbrite.com/platform/api#/reference/event-search/search-events

# First, save the base url for future use
baseURL = "https://www.eventbriteapi.com/v3"


# Let's set the following query parameters
query="python"
location = "Melbourne"
proximity = "100km"
q_startdate = "2019-02-19T00:00:00Z"
q_enddate = "2019-03-01T00:00:00Z"

# then we create the url with these parameters
url = "{0}/events/search?q={1}&location.address={2}&location.within={3}&start_date.range_start={4}&start_date.range_end={5}".format(
    baseURL, query, location, proximity, q_startdate, q_enddate)

## use try/except to catch any connection or timeout errors.
try:
    call = requests.get(url, headers=headers) # We're GET because we are effectively getting data from Eventbrite
    print("Succesful connection", url)
except requests.exceptions.RequestException as err:
    '''
    This except is going to catch instances where there is a connection error.
    Other possible requests exceptions: HTTPError, ConnectionError, Timeout
    '''
    print("Ooops: Something went wrong",err)
