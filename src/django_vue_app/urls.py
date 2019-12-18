"""django_vue_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token, verify_jwt_token

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),

    url(r'^api/v1/auth/obtain_token/', obtain_jwt_token),
    url(r'^api/v1/auth/refresh_token/', refresh_jwt_token),
    url(r'^api/v1/auth/token-verify/', verify_jwt_token),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
