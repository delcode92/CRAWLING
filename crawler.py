import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

class SimpleCrawler:
    def __init__(self, start_url, max_depth=2):
        self.start_url = start_url
        self.max_depth = max_depth
        self.visited_urls = set()

    def crawl(self, url, depth):
        if depth > self.max_depth:
            return
        if url in self.visited_urls:
            return

        print(f'Crawling: {url} at depth {depth}')
        self.visited_urls.add(url)

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f'Failed to fetch {url}: {e}')
            return

        page_content = response.text
        soup = BeautifulSoup(page_content, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            if self.is_valid_url(full_url):
                self.crawl(full_url, depth + 1)

    def is_valid_url(self, url):
        parsed_url = urlparse(url)
        return bool(parsed_url.netloc) and bool(parsed_url.scheme)

if __name__ == '__main__':
    start_url = 'https://facebook.com'
    crawler = SimpleCrawler(start_url, max_depth=3)
    crawler.crawl(start_url, 0)

