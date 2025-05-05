"Django view for the todo list application."
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

class TaskList(ListView):
    "Django view for displaying a list of tasks."
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    "Django view for displaying the details of a task."
    model = Task
    context_object_name = 'task'
    # template_name = 'base/task_detail.html'
