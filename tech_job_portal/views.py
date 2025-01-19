# jobs/views.py

from django.shortcuts import render
from .models import Job
from .scraper import scrape_indeed_jobs
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Save scraped job data to the database
def save_jobs(request):
    job_list = scrape_indeed_jobs('software developer', 'remote')
    for job_data in job_list:
        Job.objects.update_or_create(
            title=job_data['title'],
            company=job_data['company'],
            location=job_data['location'],
            defaults={'salary': job_data['salary'], 'url': job_data['url']}
        )
    return render(request, 'jobs/save_jobs.html', {'jobs': job_list})

# Display the job listings
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# Visualize job data as a bar chart
def job_chart(request):
    jobs_by_company = Job.objects.values('company').annotate(count=models.Count('company'))
    companies = [job['company'] for job in jobs_by_company]
    counts = [job['count'] for job in jobs_by_company]

    plt.figure(figsize=(10, 5))
    plt.bar(companies, counts, color='skyblue')
    plt.xlabel('Company')
    plt.ylabel('Number of Job Postings')
    plt.title('Job Postings by Company')
    plt.xticks(rotation=45, ha='right')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    chart = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'jobs/job_chart.html', {'chart': chart})
