# The Verge Web Scraper

This is a web scraper for The Verge website that extracts article titles, authors, and dates published and saves them to a CSV file.

## Installation

1. Clone the repository: `git clone https://github.com/Suhaan-Bhandary/theverge-web-scrapper.git`
2. Navigate to the project directory: `cd theverge-web-scrapper`
3. Create a virtual environment using Python: `python -m venv env`
4. Activate the virtual environment: `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate` (Windows)
5. Install the required packages: `pip install -r requirements.txt`

## Usage

1. Activate the virtual environment: `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate` (Windows)
2. Navigate to the project directory: `cd theverge-web-scraper`
3. Run the `scraper.py` file: `python scraper.py`
4. Wait for the program to complete. Once finished, the scraped data will be saved to a CSV file in the `data` directory and the SQLite database in `data` directory.

### Note

If python is not working trying using python3 and pip3 in place of python and pip
