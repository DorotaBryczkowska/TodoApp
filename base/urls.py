'# Django URL configuration for the base app'
from django.urls import path
from .views import TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
]
