from django.urls import path, include
# from views import register
from .views import register, login_user, index, logout_user

urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout")
]