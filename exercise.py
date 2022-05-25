# The goal of today is to be able to use web scraping to find a specific element on a web page, convert the data, and enter it into an excel spreadsheet.  
# This is not an easy assignment, and will require you to refer to the notes and documentation you have been working with for the past 3 weeks.
import requests

url = "https://motorcycle-specs-database.p.rapidapi.com/model/make-id/100/2015/Sport"

headers = {
	"X-RapidAPI-Host": "motorcycle-specs-database.p.rapidapi.com",
	"X-RapidAPI-Key": "c6d3bf4ed2mshdabd204c75b404dp15dc0bjsn61acd9c567ed"
}

response = requests.request("GET", url, headers=headers)

print(response.text)