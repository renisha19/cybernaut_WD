# jobs/scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_indeed_jobs(query, location):
    url = f'https://www.indeed.com/jobs?q={query}&l={location}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_elements = soup.find_all('div', class_='jobsearch-SerpJobCard')

    jobs = []
    for job_elem in job_elements:
        title = job_elem.find('h2', class_='title').text.strip() if job_elem.find('h2', class_='title') else 'N/A'
        company = job_elem.find('span', class_='company').text.strip() if job_elem.find('span', 'company') else 'N/A'
        location = job_elem.find('div', class_='location').text.strip() if job_elem.find('div', 'location') else 'N/A'
        salary = job_elem.find('span', class_='salaryText').text.strip() if job_elem.find('span', 'salaryText') else 'N/A'
        url = "https://www.indeed.com" + job_elem.find('a')['href'] if job_elem.find('a') else None

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'salary': salary,
            'url': url
        })
    return jobs
