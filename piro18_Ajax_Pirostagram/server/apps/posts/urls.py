from django.urls import path
from . import views 

app_name = "posts"

urlpatterns = [
    path('', views.main, name="main"),
    path('post_create/', views.post_create, name="post_create"),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('del_comment_ajax/', views.del_comment_ajax, name="del_comment_ajax"),
    path('create_comment_ajax/', views.create_comment_ajax, name='create_comment_ajax')
]