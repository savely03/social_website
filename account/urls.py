from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordChangeView, \
    PasswordChangeDoneView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-then-login/', logout_then_login, name='logout-then-login'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.dashboard, name='dashboard'),
]
