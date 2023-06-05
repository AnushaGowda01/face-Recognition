from PIL import Image
import pytesseract

image = 'test1.png'
text = pytesseract.image_to_string(Image.open(image), lang="eng")
print(text)