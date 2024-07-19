from django.urls import path
from users.views import CustomLogin
urlpatterns = [
    # 登录界面
    path("login", CustomLogin.as_view()),
]