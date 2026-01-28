import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

# 1. Render the main page
def index(request):
    return render(request, 'tasks/index.html')

# 2. API: List all tasks
def get_tasks(request):
    tasks = Task.objects.all().values('id', 'title', 'created_at').order_by('-created_at')
    return JsonResponse(list(tasks), safe=False)

# 3. API: Add a task
@csrf_exempt # Disabling CSRF for simplicity in this specific challenge
def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        if title:
            task = Task.objects.create(title=title)
            return JsonResponse({'id': task.id, 'title': task.title, 'message': 'Task created!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# tasks/views.py (Add this to the bottom)

@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return JsonResponse({'message': 'Task deleted successfully!'})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)