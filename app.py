from flask import Flask
from services.airbnb_img_scraper import ImagesScraper
from services.gvision import ImageVision
app = Flask(__name__)

test_url = "https://www.airbnb.fr/rooms/31348954?check_in=2022-02-11&check_out=2022-02-12&previous_page_section_name=1000&federated_search_id=3c0640f4-2d24-482b-9763-d105595834b4&guests=1&adults=1"
@app.route('/')

def test_route():
	return test_url


# a GET Request to trigger the 
@app.route('/isworkable/<path:airbnb_url>')

def get_airbnb_analysis(airbnb_url):
	'''Scrapes the pictures form url parameter
	Sends the pictures to Google Vision API
	Parses the data from Google Vision
	Returns the parsed data as a JSON file '''	

	# beautiful soup opens the url + /photos
	# get the url of each photo
	scraper = ImagesScraper(airbnb_url)
	images_urls = scraper.scrape_images()	

	# send the photos to google vision
	img_analyser = ImageVision(images_urls)
	found_items = img_analyser.analyse_images()
	

	return " ".join([item for item in found_items])
	pass


app.run(port=5000)