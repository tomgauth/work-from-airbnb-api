import pytest
from flask import Flask

from handlers.routes import configure_routes


def test_get_airbnb_analysis():
	listing_url = 'https://www.airbnb.fr/rooms/669432?previous_page_section_name=1000&federated_search_id=3c7e1b61-76bb-457e-8d07-44fd686096ba&guests=1&adults=1'
	app = Flask(__name__)
	configure_routes(app)
	client = app.test_client()
	url = '/isworkable/https://www.airbnb.fr/rooms/669432?previous_page_section_name=1000&federated_search_id=3c7e1b61-76bb-457e-8d07-44fd686096ba&guests=1&adults=1'
	response = client.get(url)
	assert response.get_data() == b'Table'