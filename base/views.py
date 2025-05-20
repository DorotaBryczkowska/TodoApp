"Django view for the todo list application."
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task

class CustomLoginView(LoginView):
    "Django view for custom login page."
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
  
class RegisterPage(FormView):
    "Django view for user registration."
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    "Form validation to log in the user after registration."
   # def form_valid(self, form):
   #     user = form.save()
   #     if user is not None:
   #         login(self.request, user)
   #     return super(RegisterPage, self).form_valid(form)

class TaskList(LoginRequiredMixin, ListView):
    "Django view for displaying a list of tasks."
    model = Task
    context_object_name = 'tasks'

    "User-specific task filtering."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    "Django view for displaying the details of a task."
    model = Task
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    "Django view for creating a new task."
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    "Form validation to set the user."
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    "Django view for updating an existing task."
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    "Django view for deleting a task."
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
