"Django view for the todo list application."
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Task

class TaskList(ListView):
    "Django view for displaying a list of tasks."
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    "Django view for displaying the details of a task."
    model = Task
    context_object_name = 'task'

class TaskCreate(CreateView):
    "Django view for creating a new task."
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    "Django view for updating an existing task."
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
