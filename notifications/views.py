from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(user=request.user, read=False)
    data = [{"message": n.message, "created_at": n.created_at} for n in notifications]
    return JsonResponse({"notifications": data})