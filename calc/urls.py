from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('teacher',views.teacher,name = 'teacher'),
    path('student',views.student,name= 'student')

]