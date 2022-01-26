import requests
from bs4 import BeautifulSoup


class ImagesScraper:
	""" Simple scraper that returns all the images
	from a listing"""

	def __init__(self, listing_url):
		path = '/photos' if listing_url[-1] != '/' else 'photos'
		self.url = listing_url + path

	def scrape_images(self):
		images_urls = []
		r = requests.get(self.url)
		soup = BeautifulSoup(r.text, 'html.parser')
		img_tags = soup.find_all('img')
		urls = [img['src'] for img in img_tags]
		return urls
