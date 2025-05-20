# Crawl-DSA

This project is a Python script that automates the process of converting web pages into PDF files. It uses the Playwright library to navigate to URLs and save the content as PDF files.

## Features

- Reads a list of URLs from a text file (`urls.txt`).
- Converts each URL into a PDF file.
- Automatically organizes the PDFs into folders based on the URL structure.

## Requirements

- Python 3.7 or higher
- Playwright library

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd crawl-DSA
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install playwright
   ```

## Usage

1. Add the URLs you want to convert to `urls.txt`, one URL per line.
2. Run the script:
   ```bash
   python main.py
   ```
3. The PDFs will be saved in folders based on the URL structure.

## Output Structure

The script organizes the output PDFs into folders based on the first segment of the URL path. For example:

- URL: `http://example.com/algebra/aho_corasick.html`
- Output: `algebra/aho_corasick.pdf`

## Notes

- Ensure that the URLs in `urls.txt` are accessible and valid.
- The script uses the Chromium browser provided by Playwright.

## License

This project is licensed under the MIT License.
