import pytest
from app import app


def test_get_airbnb_analysis():
	test_url = 'https://www.airbnb.fr/rooms/669432?previous_page_section_name=1000&federated_search_id=3c7e1b61-76bb-457e-8d07-44fd686096ba&guests=1&adults=1'
	assert app.get_airbnb_analysis(test_url) == "Table"