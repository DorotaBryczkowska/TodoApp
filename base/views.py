"Django view for the todo list application."
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from .models import Task

class CustomLoginView(LoginView):
    "Django view for custom login page."
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

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

class TaskDelete(DeleteView):
    "Django view for deleting a task."
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
