import pytesseract
from urllib import request
from PIL import Image
import time

def main():
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    url ="https://passport.lagou.com/vcode/create?from=login&refresh=1534430790484"
    print(url)
    while True:
        request.urlretrieve(url,'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)
if __name__ == '__main__':
    main()