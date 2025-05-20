import os
from urllib.parse import urlparse
from pathlib import Path
from playwright.sync_api import sync_playwright

input_file = "urls.txt"

def save_pdf_path(url: str) -> Path:
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")  # ['string', 'aho_corasick.html']
    folder = path_parts[0] if len(path_parts) > 1 else ""
    filename_html = path_parts[-1]  # 'aho_corasick.html'
    filename = Path(filename_html).with_suffix(".pdf").name  # 'aho_corasick.pdf'
    if folder:
        os.makedirs(folder, exist_ok=True)
        return Path(folder) / filename
    else:
        return Path(filename)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    with open(input_file, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    count = 0  # Biến đếm số file đã tải
    for url in urls:
        page.goto(url, wait_until="networkidle")
        pdf_path = save_pdf_path(url)
        page.pdf(path=str(pdf_path), format="A4", print_background=True)
        count += 1
        print(f"Đã lưu PDF của {url} tại {pdf_path}")

    browser.close()

print(f"Tổng số file PDF đã tải: {count}")
