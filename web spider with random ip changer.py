import requests
from bs4 import BeautifulSoup
import random

class WebCrawler:
    def __init__(self):
        self.base_url = "http://www.example.com"

    def get_random_ip(self):
        # Generate a random IP address
        ip = ".".join([str(random.randint(0, 255)) for _ in range(4)])
        return ip

    def crawl(self, url):
        try:
            # Use a random IP address to make the request
            headers = {"X-Forwarded-For": self.get_random_ip()}
            source_code = requests.get(url, headers=headers)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")

            # Print page details
            page_title = soup.title.text.strip()
            print(f"Page Title: {page_title}\n")
            self.print_paragraphs(soup.find_all("p"))
        except requests.RequestException as req_err:
            print("Request Error:", req_err)
        except Exception as e:
            print("An error occurred:", e)

    def print_paragraphs(self, paragraphs):
        if paragraphs:
            print("Page Summary:")
            for idx, paragraph in enumerate(paragraphs, start=1):
                text = paragraph.get_text().strip()
                print(f"{idx}. {text}\n")

if __name__ == "__main__":
    web_crawler = WebCrawler()
    web_crawler.crawl(web_crawler.base_url)
