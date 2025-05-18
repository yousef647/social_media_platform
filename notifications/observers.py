# notifications/observers.py
from abc import ABC, abstractmethod
from notifications.models import Notification

# Abstract Observer
class Observer(ABC):
    @abstractmethod
    def update(self, event, data):
        pass

# Concrete Observer for Notifications
class NotificationObserver(Observer):
    def __init__(self, user):
        self.user = user

    def update(self, event, data):
        if event == "new_post":
            message = f"New post by {data['user'].username}: {data['content'][:20]}..."
        elif event == "new_comment":
            message = f"New comment on your post by {data['user'].username}"
        else:
            return
        Notification.objects.create(user=self.user, message=message)

# Subject to Manage Observers
class NotificationSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, event, data):
        for observer in self._observers:
            observer.update(event, data)