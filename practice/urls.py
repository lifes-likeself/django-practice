"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path, path, include
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar



urlpatterns = [
    path('admin/', admin.site.urls),  # <<???
    path('account/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('dojo/', include('dojo.urls')),
    re_path('__debug__/', include(debug_toolbar.urls)), #9강.. 어떻게 해야함.
]
