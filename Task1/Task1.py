import sys 
from PIL import Image;
import pytesseract

def extractText(imagepath):
    try:
        image = Image.open(imagepath)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as ex:
        return f"error{ex}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    imagepath = sys.argv[1]

    text = extractText(imagepath)
    print(text)
