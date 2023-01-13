from django.urls import path
from server.apps.posts.views import posts_main, posts_review, posts_create, posts_detail, posts_delete, posts_update

urlpatterns = [
   path('', posts_main),
   path("review", posts_review),
   path("review/create", posts_create),
   path("review/<int:pk>", posts_detail ),
   path("review/<int:pk>/delete", posts_delete),
   path("review/<int:pk>/update", posts_update),
]