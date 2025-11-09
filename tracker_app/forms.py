# tracker_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import LogEntry

class RegisterForm(UserCreationForm):
    # We can add more fields here later (like email), but for now,
    # the default UserCreationForm (username, password 1, password 2) is perfect.
    class Meta:
        model = User
        fields = ['username'] # We only need the username for this simple form

class LogEntryForm(forms.ModelForm):
    class Meta:
        model = LogEntry
        # Show these fields on the form
        fields = ['log_type', 'test_result', 'notes']
        # Add a user-friendly label for 'log_type'
        labels = {
            'log_type': 'Log Type',
            'test_result': 'Test Result (e.g., "120 mg/dL")',
            'notes': 'Notes (e.g., "Ate 1 apple" or "Feeling tired")',
        }
        # Make 'test_result' not required
        widgets = {
            'test_result': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }        