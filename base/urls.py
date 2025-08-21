from django.urls import path
from .views import registerView, home, loginView, logoutView
# REMOVA estas duas linhas daqui
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path("signup/", registerView, name="register"), 
    path("login/",loginView, name="login"),
    path('logout/', logoutView, name='logout'), 
]
# E REMOVA a linha "+ static(...)" daqui