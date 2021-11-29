# Ticket-Viewer

## Intro

This script is designed to fetch and display the ticktes from Zendesk platform through Zendesk API.  
It has two basic funtions, which are displaying ticktes list page by page and search specific ticket by its ID.  

## Set up

* Install Python3
* run commands: `python -m pip install dotenv`
* run commands: `python -m pip install requests`
* run commands: `python -m pip install urllib`
* edit .env file, make sure that 'MAILBOX = "your username", PASSWORD = "your password", DOMAIN = "your Zendesk URL prefix"'.

## Usage

* run commands at the root path of this repository: `python TicketsController.py`, and follow the instructions.

## Demo

![Page Display]()
we got 4 page total results, with the data provide in [Test JSON](https://gist.github.com/svizzari/c7ffed8e10d3a456b40ac9d18f34289c).  
There are totally 100 tickets, and 25 tickets in each page.  

## Ref

[Zendesk Doc](https://developer.zendesk.com/rest_api/docs/support/tickets)