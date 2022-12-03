# This is the database file
#https://docs.google.com/spreadsheets/d/13AU6tbAudnYdcr1Avl0DTbXAaOEW1pSpP1nK8x7Ov2M/edit?usp=sharing

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time
import datetime
import os
import sys
import json
import requests
import urllib
import urllib2

# Use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("test").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

#start building html pages
#add the table from the google sheet


#https://docs.google.com/spreadsheets/d/13AU6tbAudnYdcr1Avl0DTbXAaOEW1pSpP1nK8x7Ov2M/edit?usp=sharing

