from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .forms import RegisterForm, LogEntryForm  
from .models import LogEntry                 
from django.contrib.auth.decorators import login_required 
from django.utils import timezone

# Add this new function
def register(request):
    """Register a new user."""
    if request.method == 'POST':
        # The form was submitted with data
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Form data is valid - save the user
            user = form.save()
            # Log the user in automatically
            login(request, user)
            # Send them to the homepage
            return redirect('index') 
    else:
        # User is visiting the page for the first time
        form = RegisterForm()
    
    # Pack the form into a dictionary to send to the template
    context = {'form': form, 'title': 'Register'}
    return render(request, 'tracker_app/register.html', context)
@login_required # This decorator blocks users who aren't logged in
def dashboard(request):
    """Shows the user's dashboard with their logs and a form to add new ones."""
    
    # Handle the form submission (POST request)
    if request.method == 'POST':
        form = LogEntryForm(request.POST)
        if form.is_valid():
            # Don't save to database yet
            new_log = form.save(commit=False) 
            # Assign the currently logged-in user to the log
            new_log.user = request.user 
            new_log.save()
            # Redirect back to the same page to clear the form
            return redirect('dashboard') 
    else:
        # User is just visiting (GET request), show a blank form
        form = LogEntryForm()

    # Get all log entries for the CURRENT logged-in user, newest first
    logs = LogEntry.objects.filter(user=request.user).order_by('-timestamp')

    context = {
        'title': 'My Log',
        'form': form,
        'logs': logs,
    }
    return render(request, 'tracker_app/dashboard.html', context)

@login_required
def print_report(request):
    """Generates a clean, printable report of all the user's logs."""
    
    # Get all log entries for the CURRENT logged-in user, oldest first
    logs = LogEntry.objects.filter(user=request.user).order_by('timestamp')
    
    # Get the current date to display on the report
    today = timezone.now().date()

    context = {
        'title': 'My Health Report',
        'logs': logs,
        'report_date': today,
        'user': request.user,
    }
    return render(request, 'tracker_app/print_report.html', context)