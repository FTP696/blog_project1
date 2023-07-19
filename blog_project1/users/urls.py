
from django.urls import path
#importamos loginview
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistroView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'usuarios/login.html'), name = 'login' ),
    path('logout/', LogoutView.as_view(next_page = '../login'), name = 'logout' ),
    path('register/', RegistroView.as_view(), name = 'register' ),
]