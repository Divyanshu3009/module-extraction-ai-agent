import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


class DocumentationCrawler:
    def __init__(self, base_url, max_depth=1):
        self.base_url = base_url
        self.base_domain = urlparse(base_url).netloc
        self.max_depth = max_depth
        self.visited = set()
        self.pages = {}

    def crawl(self):
        """
        Entry point for crawling.
        """
        self._crawl_recursive(self.base_url, depth=0)
        return self.pages

    def _crawl_recursive(self, url, depth):
        if depth > self.max_depth:
            return

        if url in self.visited:
            return

        self.visited.add(url)
        print(f"Crawling: {url}")

        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return
        except requests.RequestException:
            return

        soup = BeautifulSoup(response.text, "html.parser")
        self.pages[url] = soup

        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            parsed = urlparse(next_url)

            if parsed.netloc != self.base_domain:
                continue

            clean_url = parsed.scheme + "://" + parsed.netloc + parsed.path

            if clean_url not in self.visited:
                self._crawl_recursive(clean_url, depth + 1)
