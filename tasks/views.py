from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm, UpdateForm, SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from datetime import datetime

# Create your views here.

def index(request):
    now=datetime.now()
    
    try:
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'index.html',{'tasks':tasks,'now':now})
    except:
        return render(request, 'index.html')
@login_required      
def add(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            
            task = form.save()
            
            task.name = form.cleaned_data['name']
            task.description = form.cleaned_data['description']
            task.image = form.cleaned_data['image']
            task.dueDate = form.cleaned_data['dueDate']
            task.is_priority = form.cleaned_data['is_priority']
            task.user= request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()    
    return render(request, 'addTask.html', {'form':form})
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task,id=task_id, user=request.user)
    task.user = request.user
    task.delete()
    return redirect('index')
 
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = form.cleaned_data['username']
            user.password = form.cleaned_data.get('password1')
            user.email = form.cleaned_data.get('email')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.set_password(password)
            user.save()
            user = authenticate( password=user.password, username=user.username)
            login(request, user)
            messages.success(request, ("Registration successful :)..."))
            return redirect('index')
        else:
            messages.error(request, ("There was an error with your registration, please try again..."))
            return redirect('register_user')
    else:
        return render(request, 'register.html', {'form': form})
   
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user.set_password(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in :)..."))
            return redirect('index')
        else:
            messages.error(request, ("There was an error logging in, please try again..."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out :)..."))
    return redirect('index')


def update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
      
        name= request.POST.get('name')
        description= request.POST.get('description')
        image= request.FILES.get('image')
        is_complete = request.POST.get('is_complete') == 'on'  # Convert checkbox value to boolean
        dueDate= request.POST.get('dueDate')
        category = request.POST.get('category')
        if category:
            try:
                task.category=Category.objects.get(id=category)
            except:
                task.category=None
        if dueDate:
            task.dueDate=dueDate
        if image:
            task.image = image
        if name:
            task.name = name
        if description:
            task.description = description
        if is_complete:
            task.is_complete = True
        else:
            task.is_complete = False
      
            
        task.save()
        messages.success(request, ("Task updated successfully :)..."))
        return redirect('index',)    
    else:
        form2= UpdateForm(instance=task)
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'task.html', {'form2': form2,'task':task})   
