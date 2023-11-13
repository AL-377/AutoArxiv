'''
This file contains the ArxivScraper class responsible for scraping papers from arXiv.
'''
import requests
from bs4 import BeautifulSoup
import time
class ArxivScraper:
    def __init__(self):
        self.domains = []
        self.update_interval = 0
        self.papers = []
        self.running = False
    def set_domains(self, domains):
        self.domains = domains
    def set_update_interval(self, interval):
        self.update_interval = interval
    def start(self):
        self.running = True
        while self.running:
            self.scrape_papers()
            time.sleep(self.update_interval * 60)
    def stop(self):
        self.running = False
    def scrape_papers(self):
        self.papers = []
        for domain in self.domains:
            url = f"https://arxiv.org/search/?query={domain}&searchtype=all&abstracts=show&order=-announced_date_first"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            results = soup.find_all("li", class_="arxiv-result")
            for result in results:
                title = result.find("p", class_="title is-5 mathjax").text.strip()
                abstract = result.find("span", class_="abstract-full has-text-grey-dark mathjax").text.strip()
                link = result.find("p", class_="list-title is-inline-block").a["href"]
                paper = f"{title}[SPLIT]{abstract}[SPLIT]{link}"
                self.papers.append(paper)
    def filter_papers(self, domain):
        filtered_papers = []
        for paper in self.papers:
            if domain.lower() in paper.lower():
                filtered_papers.append(paper)
        return filtered_papers