import pytesseract
from PIL import Image





pytesseract.pytesseract.tesseract_cmd=r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

imge =Image.open('a.png')
text =pytesseract.image_to_string(imge)
#text =pytesseract.image_to_string(imge,lang='chi_sim')
print(text)