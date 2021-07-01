from users.models import Expert
from django.urls import path

from .views import ExpertView, SocialUserView 

urlpatterns = [
    path('/social-login', SocialUserView.as_view()),
    path('/expert', ExpertView.as_view())
]