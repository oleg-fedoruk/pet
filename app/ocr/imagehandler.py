from pathlib import Path

from PIL import Image

import pytesseract

path = Path(__file__)
parent = path.parent.parent
path_to_image_test = parent / 'media/test.png'
path_to_image_pass = parent / 'media/pass.jpg'

print(pytesseract.image_to_string(Image.open(path_to_image_test)))

print(pytesseract.image_to_string(Image.open(path_to_image_pass)))


if __name__ == '__main__':
    pass
