from django.urls import path
from notifications.views import get_notifications

urlpatterns = [
    path("get/", get_notifications, name="get_notifications"),
]