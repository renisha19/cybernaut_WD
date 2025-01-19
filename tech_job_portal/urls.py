# tech_job_portal/urls.py
from django.contrib import admin
from django.urls import path, include  # 'include' is used to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('jobs/', include('jobs.urls')),  # Include the job app URLs here
]
