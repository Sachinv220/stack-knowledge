from django.urls import path 
from . import views


app_name = "stack"

urlpatterns = [
    path("ask/", views.ask_question, name="ask"),
    path("feed/", views.feed, name="feed"), 
    path("comments/<int:num>/",views.view_comments, name="comments"),
    path("posts/", views.user_posts, name="posts"), 
    path("delete/<int:id>/", views.delete_post, name="delete"), 
]
