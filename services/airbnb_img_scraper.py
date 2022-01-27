import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup


class ImagesScraper:
	""" Simple scraper that returns all the images
	from a listing"""

	def __init__(self, listing_url):
		path = 'photos' if listing_url.endswith('/') else '/photos'
		self.url = listing_url + path

	def scrape_images(self):		
		images_urls = []
		try:
			r = requests.get(self.url)
		except MissingSchema:
			return "The Url you provided is incorrect"

		soup = BeautifulSoup(r.text, 'html.parser')
		img_tags = soup.find_all('img')
		urls = [img['src'] for img in img_tags]
		return urls
