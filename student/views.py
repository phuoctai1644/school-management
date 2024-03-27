from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from student.models import Student
from django.urls import reverse


class StudentListView(ListView):
    template_name = 'list.html'
    model = Student
    context_object_name = 'students'


def student_list(request):
    student_obj = Student.objects.all()

    if request.method == 'GET':
        return render(request, 'list.html', {'students': student_obj})
    elif request.method == 'POST':
        form_data = {}
        for key in request.POST:
            form_data[key] = request.POST[key]
        new_student = Student(
            name=form_data['name'],
            age=form_data['age'],
            sex=form_data['sex'],
            avatar=request.FILES['avatar']
        )
        new_student.save()
        return HttpResponseRedirect(reverse('student:List'))


def student_detail(request, pk):
    student_obj = Student.objects.get(id=pk)
    return render(request, 'detail.html', {'student': student_obj})
