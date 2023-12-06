'''
This file contains the Visual class for managing the visual aspects of the supermarket sales management system.
'''
from PIL import Image
class Visual:
    def __init__(self):
        # Code to initialize the visual class
        pass
    def display_product_image(self, product):
        # Code to display the image of a product
        image_path = f"{product}.jpg"  # Replace with the actual path to the image file
        image = Image.open(image_path)
        image.show()