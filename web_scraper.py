# Import modules
from bs4 import BeautifulSoup
import requests
# Import page url
url = "https://realpython.github.io/fake-jobs/"
# Scrape and parse html
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
jobs = soup.find_all("h2")
job_elements = [
    h2_element.parent.parent.parent for h2_element in jobs
]
# Print Scraped stuff
for job_element in job_elements:
    title = job_element.find("h2", class_="title").text.strip()
    company = job_element.find("h3", class_="company").text.strip()
    location = job_element.find("p", class_="location").text.strip()
    time = job_element.find("time").text.strip()
    link_url = job_element.find_all("a")[1]["href"]

    print(title)
    print(company)
    print(location)
    print(time)
    print(f"Apply here: {link_url}\n")
    print()