from django.urls import path
from posts.views import create_post, create_comment

urlpatterns = [
    path("create/", create_post, name="create_post"),
    path("comment/<int:post_id>/", create_comment, name="create_comment"),
]