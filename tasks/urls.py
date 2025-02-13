from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name = 'task_list'),
    path('add/' , views.add_task, name = 'add_task'),
    path('<int:task_id>/complete/', views.complete_task, name = 'complete_task'),

]