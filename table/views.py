from django.http import HttpResponse
from .models import Task
from django.shortcuts import render


def day_task(request,day):
    daily_task = Task.objects.get(day=day)
    return HttpResponse(f"{daily_task.task}")