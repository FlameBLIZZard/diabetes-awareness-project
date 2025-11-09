# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Corresponds to @main_bp.route('/') from your report
    path('', views.index, name='index'), 
    
    # Corresponds to @main_bp.route('/types-of-diabetes')
    path('types-of-diabetes/', views.types_of_diabetes, name='types_of_diabetes'),
    
    # Corresponds to @main_bp.route('/symptoms-and-prevention')
    path('symptoms-and-prevention/', views.symptoms_and_prevention, name='symptoms_and_prevention'),
    
    # Corresponds to @main_bp.route('/healthy-diet')
    path('healthy-diet/', views.healthy_diet, name='healthy_diet'),
]