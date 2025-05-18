# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from posts.models import Post, Comment
# from notifications.models import Notification
#
# @login_required
# def create_post(request):
#     if request.method == "POST":
#         content = request.POST.get("content")
#         image = request.FILES.get("image")
#         post = Post.objects.create(user=request.user, content=content, image=image)
#         # Create notification for user (e.g., followers could be added)
#         Notification.objects.create(
#             user=request.user,
#             message=f"You created a new post"
#         )
#         return redirect("home")
#     return render(request, "home.html")
#
# @login_required
# def create_comment(request, post_id):
#     if request.method == "POST":
#         content = request.POST.get("content")
#         post = Post.objects.get(id=post_id)
#         Comment.objects.create(post=post, user=request.user, content=content)
#         # Create notification for post owner
#         Notification.objects.create(
#             user=post.user,
#             message=f"{request.user.username} commented on your post"
#         )
#         return redirect("home")
#     return redirect("home")


##########################################################################################################################################
# posts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from notifications.observers import NotificationSubject, NotificationObserver
from users.models import CustomUser

@login_required
def create_post(request):
    subject = NotificationSubject()
    # Attach all users as observers except the current user
    users = CustomUser.objects.exclude(id=request.user.id)
    for user in users:
        subject.attach(NotificationObserver(user))

    if request.method == "POST":
        content = request.POST.get("content")
        image = request.FILES.get("image")
        post = Post.objects.create(user=request.user, content=content, image=image)
        # Notify observers of the new post
        subject.notify("new_post", {"user": request.user, "content": content})
        return redirect("home")
    return render(request, "home.html")

@login_required
def create_comment(request, post_id):
    subject = NotificationSubject()
    post = Post.objects.get(id=post_id)
    # Notify the post owner (if not the commenter)
    if post.user != request.user:
        subject.attach(NotificationObserver(post.user))

    if request.method == "POST":
        content = request.POST.get("content")
        comment = Comment.objects.create(post=post, user=request.user, content=content)
        # Notify the post owner of the new comment
        subject.notify("new_comment", {"user": request.user, "post": post})
        return redirect("home")
    return render(request, "design_proj/home.html")