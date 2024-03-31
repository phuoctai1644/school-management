from django.shortcuts import render, redirect
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
        return redirect('student:List')


def student_detail(request, pk):
    student_obj = Student.objects.get(id=pk)
    return render(request, 'detail.html', {'student': student_obj})


def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('student:List')


def edit_student(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(id=pk)
        fields = [field.name for field in student._meta.get_fields()]
        except_field = ['id', 'avatar']
        for field in fields:
            if field not in except_field and getattr(student, field) and request.POST.get(field) is not None:
                setattr(student, field, request.POST[field])

        if request.FILES and request.FILES['avatar']:
            setattr(student, 'avatar', request.FILES['avatar'])
        student.save()

    redirect_url = reverse('student:Detail', kwargs={'pk': pk})
    return redirect(redirect_url)
