"""sapfluxnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from sfnform import views as sfnform_views
from home import views as home_views


#from . import views

urlpatterns = [
    url(r'^form/$', sfnform_views.built_form, name='form'),
    url(r'^uploadform/$', sfnform_views.upload_form, name='uploadform'),
    url(r'^thanks/$', TemplateView.as_view(template_name="sfnform/thanks.html"), name='thanks'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^$', home_views.index, name='index'),
    url(r'^team/$', home_views.team, name='team'),
]
