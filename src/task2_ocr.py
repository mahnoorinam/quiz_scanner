import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
import re
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=10)
    enhanced = cv2.convertScaleAbs(denoised, alpha=1.5, beta=20)
    _, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    temp_path = image_path.replace(".jpeg", "_processed.jpg").replace(".jpg", "_processed.jpg")
    cv2.imwrite(temp_path, thresh)
    return temp_path

def extract_student_info(image_path):
    processed = preprocess_image(image_path)
    
    configs = [
        '--psm 6 --oem 3',
        '--psm 4 --oem 3',
        '--psm 11 --oem 3',
    ]
    
    full_text = ""
    for config in configs:
        try:
            text = pytesseract.image_to_string(Image.open(processed), config=config)
            full_text += " " + text
        except:
            pass

    full_text_original = pytesseract.image_to_string(Image.open(image_path))
    full_text += " " + full_text_original

    student_info = {"name": "", "reg": ""}

    # Registration patterns
    reg_patterns = [
        r'BSE[-\s]?FA\d{2}[-\s]?\d{3}',
        r'B[S5][E3][-\s]?FA\d{2}[-\s]?\d{3}',
        r'[A-Z]{2,4}[-\s]?FA\d{2}[-\s]?\d{3}',
        r'FA\d{2}[-\s]?\d{3}',
    ]
    
    for pattern in reg_patterns:
        reg_match = re.search(pattern, full_text, re.IGNORECASE)
        if reg_match:
            raw = reg_match.group()
            cleaned = re.sub(r'\s+', '-', raw.strip()).upper()
            if not cleaned.startswith('BSE'):
                cleaned = 'BSE-' + cleaned
            student_info["reg"] = cleaned
            break

    # Name patterns
    name_patterns = [
        r'Name[:\s]+([A-Za-z][A-Za-z\s\-\.]{3,40})(?=\s*Registration|\s*Class|\s*Time|\s*Quiz|\n|$)',
        r'Name[:\s]+([A-Za-z\s\-\.]{4,40})',
        r'[Nn]ame\s*[:\-]?\s*([A-Za-z][A-Za-z\s]{3,35})',
    ]
    
    for pattern in name_patterns:
        name_match = re.search(pattern, full_text, re.IGNORECASE)
        if name_match:
            name = name_match.group(1).strip()
            name = re.sub(r'\s+', ' ', name)
            if len(name) > 3:
                student_info["name"] = name
                break

    return student_info


if __name__ == "__main__":
    image_path = "../samples/quiz sample.jpeg"
    info = extract_student_info(image_path)
    print(f"Name: {info['name']}")
    print(f"Reg#: {info['reg']}")