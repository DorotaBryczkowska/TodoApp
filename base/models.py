"Django model for a todo list application."
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Model representing a task in the todo list.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True) #If user is deleted, all their tasks are deleted too
    title = models.CharField(max_length=200) #Title of the task
    description = models.TextField(null=True, blank=True) #Description of the task
    complete = models.BooleanField(default=False) #Whether the task is complete or not
    created = models.DateTimeField(auto_now_add=True) #Date and time when the task was created

    def __str__(self):
        return str(self.title)

    class Meta:
        """Meta options for model configuration."""
        ordering = ['complete']
