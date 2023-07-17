import requests
from bs4 import BeautifulSoup
import random

def get_random_ip():
    # Generate a random IP address
    ip = ".".join([str(random.randint(0, 255)) for _ in range(4)])
    return ip

def crawl(url: object) -> object:
    # Use a random IP address to make the request
    headers = {"X-Forwarded-For": get_random_ip()}
    source_code = requests.get(url, headers=headers)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    # Print the body of the page
    print(soup.body)
# Enter website to be crawled here
crawl("http://www.example.com")
