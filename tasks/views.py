from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from django.urls import reverse 
from django.contrib.auth import logout  # Make sure this import is here
from django.shortcuts import redirect

# User Registration View
def register(request):
     if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
              # Log the user in automatically after registration
            return redirect(reverse('login')) 
     else:
        form = UserCreationForm()
     return render(request, 'tasks/register.html', {'form': form})

# Task Management Views
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def logout_view(request):
    logout(request)  # This logs out the user
    return redirect('login') 

@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        Task.objects.create(user=request.user, title=title, description=description, due_date=due_date)
        return redirect('task_list')  # After creating the task, redirect to the task list
    return render(request, 'tasks/task_form.html')

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.status = request.POST['status']
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})



