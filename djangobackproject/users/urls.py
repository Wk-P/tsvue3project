from django.urls import path
from users.views import CustomLoginView, CustomLogoutView, CustomLoginCheck
urlpatterns = [
    # 登录界面
    path("login", CustomLoginView.as_view()),
    path("logout", CustomLogoutView.as_view()),
    path("logincheck", CustomLoginCheck.as_view()),
]