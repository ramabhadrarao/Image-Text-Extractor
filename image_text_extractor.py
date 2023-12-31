import os
import pytesseract
from PIL import Image
import re

# No need to specify the Tesseract path for Linux systems
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your Tesseract installation path

def extract_text_from_images(folder_path):
    image_texts = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if file_name.endswith('.jpg') or file_name.endswith('.png') or file_name.endswith('.jpeg'):
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img)
            image_texts.append(text)

    return image_texts

def extract_info(texts):
    pattern_name = r'Dear\s+(.*?),'
    pattern_submission_id = r'Submission ID:\s+(\d+)'

    extracted_info = []
    for text in texts:
        match_name = re.search(pattern_name, text)
        match_submission_id = re.search(pattern_submission_id, text)

        if match_name and match_submission_id:
            name = match_name.group(1)
            submission_id = match_submission_id.group(1)
            extracted_info.append(f"{name} ({submission_id})")

    return extracted_info

# Replace 'folder_path' with the path to your folder containing the images
folder_path = 'images'  # Update with your image folder path

# Extract text from images
extracted_texts = extract_text_from_images(folder_path)

# Extract names and submission IDs from the extracted text
extracted_info = extract_info(extracted_texts)

print("Extracted Information:")
for info in extracted_info:
    print(info)
