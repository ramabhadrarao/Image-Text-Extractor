# Image Text Extractor

A Python script to extract text from images using Tesseract OCR and retrieve specific information like names and submission IDs.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

This Python script utilizes Tesseract OCR to extract text from images (supports formats like jpg, png, jpeg) and performs pattern matching to extract names and submission IDs.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/repo_name.git
    cd repo_name
    ```

2. Install required libraries:

    ```bash
    pip install pytesseract Pillow
    ```

3. Tesseract Installation (if applicable):
    - For Windows: 
        - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
        - Update the Tesseract path in the code (`pytesseract.pytesseract.tesseract_cmd`) accordingly.
    - For Linux:
        - The code automatically detects Tesseract.

## Usage

1. Place your images in the 'images' folder.

2. Update the `folder_path` variable in the script with your image folder path.

3. Execute the script:

    ```bash
    python image_text_extractor.py
    ```

The script will print the extracted information from the images.

## Contributing

Feel free to contribute to this project. Contributions can be made via pull requests.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/add-something`).
3. Commit your changes (`git commit -am 'Add something'`).
4. Push to the branch (`git push origin feature/add-something`).
5. Create a new Pull Request.

## License

[MIT License](LICENSE)
