"""django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from django.views.debug import default_urlconf

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', default_urlconf),
]

admin.site.site_header = 'Shopping List'
admin.site.view_on_site = False
admin.site.site_url = None
