# Simple Web Spider in Python

A sample Python web spider project that crawls a specified website using the requests library and BeautifulSoup. This project simulates requests from random IP addresses using the X-Forwarded-For header and provides a simple way to crawl and extract the content of web pages.

## Features

- Crawl a specified website using a random IP address.
- Use the `requests` library to send HTTP requests.
- Extract and print the content of the web pages using BeautifulSoup.

## Prerequisites

- Python 3.10
- Required libraries: `requests` and `BeautifulSoup`
  - Install them using `pip install requests beautifulsoup4`

## Usage

### Setup the Project

1. Clone or download the project files to your local machine.
2. Make sure you have the required libraries installed.

### Run the Crawler

1. Open the `webspider_crawler.py` file in a Python editor or IDE.
2. Update the `url` variable in the `crawl()` function with the URL of the website you want to crawl.
3. Execute the script.

### View the Crawled Content

- The script will simulate a request from a random IP address using the X-Forwarded-For header.
- The webpage's content will be printed to the console using BeautifulSoup.

## Customization

- Modify the `url` variable in the `crawl()` function to crawl a different website.
- Adapt the script to extract specific information or perform further analysis on the crawled content as needed.

## Limitations and Legal Considerations

- Respect the terms of service and any applicable legal restrictions when crawling websites.
- Be mindful of the website's usage limits and any rate restrictions to avoid overloading the server or violating any policies.

