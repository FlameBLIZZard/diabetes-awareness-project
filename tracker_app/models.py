# tracker_app/models.py
from django.db import models
from django.contrib.auth.models import User

# These are choices for a dropdown menu to make logging easier
LOG_TYPE_CHOICES = [
    ('BG', 'Blood Glucose'),
    ('MEAL', 'Meal / Food Log'),
    ('MED', 'Medication / Insulin'),
    ('NOTE', 'General Note / Symptom'),
]

class LogEntry(models.Model):
    # This links the log entry to a specific user.
    # If the user is deleted, all their logs are deleted too (models.CASCADE).
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="log_entries")
    
    # The type of log (e.g., 'Blood Glucose', 'Meal')
    log_type = models.CharField(max_length=4, choices=LOG_TYPE_CHOICES, default='NOTE')
    
    # The date and time of the log. auto_now_add=True sets it automatically.
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # A field for test results (e.g., "120 mg/dL").
    # We make it a character field to allow for units (like "mg/dL").
    test_result = models.CharField(max_length=100, blank=True, null=True)
    
    # A field for notes, like what was eaten or how they're feeling.
    notes = models.TextField(blank=False, null=False) # 'blank=False' makes this field required

    def __str__(self):
        # This just makes it look nice in the admin panel
        return f"{self.user.username} - {self.get_log_type_display()} on {self.timestamp.strftime('%Y-%m-%d')}"