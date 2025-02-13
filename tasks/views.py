from django.shortcuts import render , get_object_or_404, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.filter(is_completed=False).order_by('due_date') 
    completed_tasks = Task.objects.filter(is_completed = True).order_by('-due_date')
    return render(request, 'task_list.html', {'tasks': tasks, 'completed_tasks':completed_tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.is_completed = True
    task.save()
    return redirect('task_list')


    
    

