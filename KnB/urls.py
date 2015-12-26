"""KnB URL Configuration

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
#coding=utf-8 
from django.conf.urls import include, url
from django.contrib import admin
from share.views import home,test_blog,login_view,go_out,diary,register_view,suggest_blog,my_info,my_group
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home),
    url(r'^test/',test_blog),
    url(r'^login/',login_view),
    url(r'^go_out.html/',go_out),
    url(r'^yj.html/',diary),
    url(r'^register/',register_view),
    url(r'^suggest/',suggest_blog),
    url(r'^personal_index/',my_info),
    url(r'^my_group/',my_group),
    
    url(r'^src/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
