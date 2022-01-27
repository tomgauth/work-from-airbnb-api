import pytest
from services.airbnb_img_scraper import ImagesScraper


def test_airbnb_img_scraper():
	image_scraper = ImagesScraper(listing_url="")
	assert image_scraper.scrape_images() == "The Url you provided is incorrect"


def test_airbnb_img_scraper_is_list():
	image_scraper = ImagesScraper(listing_url="https://www.airbnb.fr/rooms/669432")
	assert type(image_scraper.scrape_images()) is list

