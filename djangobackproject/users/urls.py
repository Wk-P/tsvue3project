from django.urls import path
from users.views import CustomLogin, CustomLogoutView, CustomLoginCheck
urlpatterns = [
    # 登录界面
    path("login", CustomLogin.as_view()),
    path("logout", CustomLogoutView.as_view()),
    path("logincheck", CustomLoginCheck.as_view()),
]