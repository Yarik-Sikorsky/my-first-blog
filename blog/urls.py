from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

]