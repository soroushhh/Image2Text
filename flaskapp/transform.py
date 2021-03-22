import os
import pytesseract
from PIL import Image


def transform_image_to_text(filename):
    """ An overall function to transform image to text """

    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    )

    try:
        text = pytesseract.image_to_string(Image.open(filename))
        return text
    except:
        return None