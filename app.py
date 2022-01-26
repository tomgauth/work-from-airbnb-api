from flask import Flask


app = Flask(__name__)


# a GET Request to trigger the 
@app.route('/isworkable')

def get_airbnb_analysis():
	'''Scrapes the pictures form url parameter
	Sends the pictures to Google Vision API
	Parses the data from Google Vision
	Returns the parsed data as a JSON file '''

	pass


app.run(port=5000)