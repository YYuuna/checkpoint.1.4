import pytesseract
from PIL import Image

img = Image.open("data/Image/image.png")
text = pytesseract.image_to_string(img)
print(text)