# main_app/views.py
from django.shortcuts import render

# Corresponds to the index() function
def index(request):
    """Homepage."""
    context = {'title': 'Home'}
    return render(request, 'main_app/index.html', context)

# Corresponds to the types_of_diabetes() function
def types_of_diabetes(request):
    """Page for Types of Diabetes."""
    context = {'title': 'Types of Diabetes'}
    return render(request, 'main_app/types.html', context)

# Corresponds to the symptoms_and_prevention() function
def symptoms_and_prevention(request):
    """Page for Symptoms & Prevention."""
    context = {'title': 'Symptoms & Prevention'}
    return render(request, 'main_app/symptoms.html', context)

# Corresponds to the healthy_diet() function
def healthy_diet(request):
    """Page for Healthy Diet."""
    context = {'title': 'Healthy Diet'}
    return render(request, 'main_app/diet.html', context)