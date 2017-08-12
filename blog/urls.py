from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #regex here is for post_detail views
    #in words: after beginning, URL should contain 'post' and a /
    #then transfer to view as variable pk
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #for forms.py
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
