from django.urls import path

from .views import SocialUserView 

urlpatterns = [
    path('/social-login', SocialUserView.as_view())
]