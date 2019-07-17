from . import views
from django.urls import path

urlpatterns = [
    path('list', views.post_list),
   #path('sum/int(x)', views.mysum),
    path('list1', views.post_list1),
    path('list2', views.post_list2),
]
