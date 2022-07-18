from django.urls import path
from applications.account.views import RegisterView, ActivationView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('active/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', LoginView.as_view())
    ]
