from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='List')
]
