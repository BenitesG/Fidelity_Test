from django.urls import path
from .views import registerView, home, loginView, logoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path("signup/", registerView, name="register"), 
    path("login/",loginView, name="login"),
    path('logout/', logoutView, name='logout'), 
] + static(settings.STATIC_URL)