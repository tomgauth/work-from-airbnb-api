from google.cloud import vision
from settings import *

class ImageVision:
    """ Class that analyses images and returns items found
    present in the items_to_find"""
    def __init__(self, images_urls, items_to_find=['Table', 'Desk', 'Office chair']):
        self.images_urls = images_urls
        self.items_to_find = items_to_find

    def analyse_images(self):
        """Analyses each image with Google Vision API"""

        client = vision.ImageAnnotatorClient()
        image = vision.Image()
        found_items = []

        for image_url in self.images_urls:

            image.source.image_uri = image_url
            response = client.label_detection(image=image)

            for label in response.label_annotations:
                item = label.description
                print(item)
                if item not in found_items and item in self.items_to_find:
                    found_items.append(item)

        return found_items
