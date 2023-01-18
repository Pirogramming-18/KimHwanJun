from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.posts_main, name="main"),
    path("posts/register_idea", views.posts_register_idea, name="register_idea"),
    path("posts/<int:pk>/idea_detail", views.posts_idea_detail, name="idea_detail"),
    path("posts/<int:pk>/tool_detail", views.posts_tool_detail, name="tool_detail"),
    path("posts/<int:pk>/idea_delete", views.posts_idea_delete, name="idea_delete"),
    path("posts/<int:pk>/idea_update", views.posts_idea_update, name="idea_update"),
    path("posts/tool_list", views.posts_tool_list, name="tool_list"),
    path("posts/register_tool", views.posts_register_tool, name="register_tool"),
    path("posts/<int:pk>/tool_delete", views.posts_tool_delete, name="tool_delete"),
    path("posts/<int:pk>/tool_update", views.posts_tool_update, name="tool_update")
    
]

