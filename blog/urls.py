from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path(r'^post/(?P<pk>[0-9]+)/$', detail, name='detail'),
    path('archives/<int:year>/<int:month>/', archives, name='archives'),
    path(r'^category/(?P<pk>[0-9]+)/$', category, name='category'),
    path(r'^tag/(?P<pk>[0-9]+)/$', tag, name='tag'),
    path('search/', search, name='search'),

    path('about', about, name='about'),
    path('contact', contact),
    path('full', full)

]
