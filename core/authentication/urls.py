from django.urls import path
from .views import LoginView, SingUpView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('singup/', SingUpView.as_view(), name='singup')
]