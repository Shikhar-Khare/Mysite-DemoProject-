from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def teacher(request):
    return render(request, 'teacher.html')

def student(request):
    return render(request, 'student.html')