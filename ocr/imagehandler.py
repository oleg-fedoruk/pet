from PIL import Image

import pytesseract

print(pytesseract.image_to_string(Image.open('/media/test.png')))

print(pytesseract.image_to_string(Image.open('/media/pass.jpg')))


if __name__ == '__main__':
    pass
