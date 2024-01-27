from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('login/', views.LoginView.as_view(), name="login_page"),
    path('Signup/', views.RegisterView.as_view(), name="Signup_page"),

]