import requests
from bs4 import BeautifulSoup

class ResearchAgent:
    def __init__(self):
        self.sources = ["https://www.hr.com", "https://www.shrm.org"]

    def fetch_trending_topics(self):
        topics = []
        for source in self.sources:
            response = requests.get(source)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                headlines = soup.find_all("h2")  # Modify based on site structure
                topics.extend([h.text for h in headlines[:5]])
        return topics

if __name__ == "__main__":
    agent = ResearchAgent()
    print(agent.fetch_trending_topics())
