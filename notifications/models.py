# from django.db import models
# from users.models import CustomUser
#
# class Notification(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     read = models.BooleanField(default=False)

#####################################################################################################
# notifications/models.py
from django.db import models
from users.models import CustomUser

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"