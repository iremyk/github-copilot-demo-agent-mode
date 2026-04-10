"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


import os
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from . import api

def api_root_url(request):
    codespace_name = os.environ.get('CODESPACE_NAME', None)
    if codespace_name:
        # Use HTTP to avoid certificate issues in the response, but actual API is served over HTTP/HTTPS as configured
        url = f"http://{codespace_name}-8000.app.github.dev/api/"
    else:
        url = "http://localhost:8000/api/"
    return JsonResponse({"api_root": url})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root_url, name='api-root-url'),
    path('', include('octofit_tracker.api')),
]
