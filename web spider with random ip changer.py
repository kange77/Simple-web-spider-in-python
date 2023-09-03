import requests
from bs4 import BeautifulSoup
import random
import logging
import time

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.user_agents = [
            "User-Agent-1",
            "User-Agent-2",
            # Add more user-agent strings here
        ]
        self.proxies = [
            "http://proxy1.example.com:8080",
            "http://proxy2.example.com:8080",
            # Add more proxy servers here
        ]
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": self.get_random_user_agent()})
        self.requests_delay = 5  # Adjust as needed
        self.max_retries = 3  # Number of retries for failed requests

        # Configure logging for advanced error handling and debugging
        logging.basicConfig(filename='web_crawler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def crawl(self, url):
        try:
            while True:
                # Use a random proxy and user-agent for each request
                self.session.headers.update({"User-Agent": self.get_random_user_agent()})
                self.session.proxies = {"http": self.get_random_proxy()}
                
                retries = 0
                while retries < self.max_retries:
                    try:
                        response = self.session.get(url)
                        response.raise_for_status()

                        soup = BeautifulSoup(response.text, "html.parser")

                        # Log page title and URL
                        page_title = soup.title.text.strip()
                        logging.info(f"Visited URL: {url}, Page Title: {page_title}")

                        # Print page details
                        print(f"Page Title: {page_title}\n")
                        self.print_paragraphs(soup.find_all("p"))
                        break
                    except requests.RequestException as req_err:
                        logging.error(f"Request Error for URL {url}: {req_err}")
                        print("Request Error:", req_err)
                        retries += 1
                        time.sleep(2 ** retries)  # Exponential backoff for retries
                else:
                    print(f"Max retries reached for URL: {url}. Skipping.")
                
                # Throttle requests to avoid overloading the server
                time.sleep(self.requests_delay)
        except KeyboardInterrupt:
            print("Crawling interrupted by the user.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            print("An unexpected error occurred. Check the log for details.")

    def print_paragraphs(self, paragraphs):
        if paragraphs:
            print("Page Summary:")
            for idx, paragraph in enumerate(paragraphs, start=1):
                text = paragraph.get_text().strip()
                print(f"{idx}. {text}\n")

if __name__ == "__main__":
    base_url = "http://www.example.com"  # You can change the URL as needed
    web_crawler = WebCrawler(base_url)

    # Perform crawling with advanced error handling, user-agent rotation, proxy rotation,
    # request throttling, and retries for failed requests
    web_crawler.crawl(web_crawler.base_url)
