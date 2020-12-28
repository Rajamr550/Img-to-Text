import pytesseract as ts
ts.pytesseract.tesseract_cmd = r'C:\pytess\tesseract.exe'
from PIL import Image

image = Image.open('Enter your image file name')
text = ts.image_to_string(image)

print(text)
