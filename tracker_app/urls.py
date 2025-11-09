# tracker_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # This will create the page at 'http://127.0.0.1:8000/tracker/register/'
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tracker_app/logged_out.html'), name='logout'),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('print-report/', views.print_report, name='print_report'),
]