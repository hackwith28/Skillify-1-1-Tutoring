from django.urls import path
from .views import UserNotificationListView

urlpatterns = [
    path('', UserNotificationListView.as_view(), name='user_notifications'),
]

