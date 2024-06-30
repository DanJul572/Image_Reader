from PIL import Image
from pytesseract import pytesseract
import enum

class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'

class ImageReader:
    def extract_text(self, image: str, lang: Language) -> str:
        img = Image.open(image)
        extracrted_text = pytesseract.image_to_string(img, lang=lang.value)
        return extracrted_text
    
    
if __name__ == '__main__':
    ir = ImageReader()
    text = ir.extract_text('images/hello.png', lang=Language.ENG)
    print(text)

