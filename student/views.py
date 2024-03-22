from django.shortcuts import render
from django.views.generic import ListView
from student.models import Student


class StudentListView(ListView):
    template_name = 'list.html'
    model = Student
    context_object_name = 'students'
