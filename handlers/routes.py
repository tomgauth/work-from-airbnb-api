from flask import Flask
from services.airbnb_img_scraper import ImagesScraper
from services.gvision import ImageVision
app = Flask(__name__)



def configure_routes(app):

	@app.route('/')
	def hello_world():
		return "Hello, world"

	# a GET Request to trigger the 
	@app.route('/isworkable/<path:airbnb_url>')
	def get_airbnb_analysis(airbnb_url):
		'''Scrapes the pictures form url parameter
		Sends the pictures to Google Vision API
		Parses the data from Google Vision
		Returns the parsed data as a JSON file 
		'''	

		# get the url of each photo
		scraper = ImagesScraper(airbnb_url)
		images_urls = scraper.scrape_images()	

		# send the photos to google vision
		img_analyser = ImageVision(images_urls)
		found_items = img_analyser.analyse_images()
		
		# returns the found items (default Table and/or Desk)
		return " ".join([item for item in found_items])
		pass


	app.run(port=5000)