from PIL import Image
import pytesseract

image_path = r'orc\a.PNG'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(Image.open(image_path), lang='kor')

print(text)

with open(r"OCR\outfile.txt","w",encoding="utf8") as f:
    f.write(text)