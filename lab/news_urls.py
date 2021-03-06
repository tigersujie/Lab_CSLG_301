"""Lab_CSLG_301 URL Configuration

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

from django.conf.urls import url
from lab import views

urlpatterns = [

    url(r'index$', views.news_index_view),
    url(r'^article$', views.news_article_view),
    url(r'^list/(\d+)$', views.news_list_view),
    url(r'^a_article$', views.achievements_article_view),
    url(r'^a_list/(\d+)$', views.achievements_list_view),
    url(r'^introduction$', views.introduction),
    url(r'^organization$', views.organization),
    url(r'^exchageproject$', views.exchageproject),
    url(r'^personhiring$', views.personhiring),

]