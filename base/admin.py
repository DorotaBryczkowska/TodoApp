"Django admin configuration for the Task model."
from django.contrib import admin
from .models import Task

admin.site.register(Task) # Register the Task model with the admin site
                            # to manage tasks through the Django admin interface.
