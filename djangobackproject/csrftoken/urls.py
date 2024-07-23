from django.urls import path
from csrftoken.views import getCSRFToken

urlpatterns = [
    path("", getCSRFToken.as_view()),
]