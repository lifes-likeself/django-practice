

from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('131231231421eq/<id>/', views.post_detail, name='post_detail'),
    #re_path(r'^(?P<id>\+d)/$', views.post_detail), 이렇게 하면 왜 안되는거지?
]