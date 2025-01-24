from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


# Create your views here.

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)

    return redirect('home')


def markTaskAsDoneOrUndone(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('home')


def deteleTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home')


def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.task = request.POST['task']
        print('Save')
        task.save()
        return redirect('home')
    else:
        completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
        incompleted_tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
        task = get_object_or_404(Task, id=pk)
        context = {
            'completed_tasks': completed_tasks,
            'incompleted_tasks': incompleted_tasks,
            'task': task
        }
        return render(request, 'edit_task.html', context=context)
