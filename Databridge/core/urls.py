from django.urls import path
from django.contrib.auth import views
from .views import index,signup,logout
urlpatterns = [
    path("",index,name="home"),
    path("signup/",signup,name="signup"),
    path("login/",views.LoginView.as_view(template_name="core/login.html"),name="login"),
    path("logout/",logout,name="logout"),
    
]