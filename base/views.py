"Django view for the todo list application."
from django.shortcuts import render
from django.http import HttpResponse

def task_list(request):
    """
    View function that returns a simple HTTP response for the todo list.
    """
    return HttpResponse("Todo List")
