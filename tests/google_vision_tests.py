import pytest
from services.gvision import ImageVision


def test_image_vision():
	urls = [
		"https://a0.muscache.com/im/pictures/miso/Hosting-36216130/original/47291782-fd62-4ab5-a398-959a2225d42c.jpeg",
		"https://a0.muscache.com/im/pictures/miso/Hosting-36216130/original/9627edfe-ee59-41d3-bfce-58458ea02daa.jpeg",
		"https://a0.muscache.com/im/pictures/miso/Hosting-36216130/original/98d7a760-450f-4499-b734-94ded1458544.jpeg"
		]
	image_vision = ImageVision(images_urls=urls)
	assert image_vision.analyse_images() == ['Office chair']
