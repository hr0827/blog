from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path(r'^post/(?P<pk>[0-9]+)/$', detail, name='detail'),

]
