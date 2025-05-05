"Django view for the todo list application."
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

class TaskList(ListView):
    "Django view for displaying a list of tasks."
    model = Task
