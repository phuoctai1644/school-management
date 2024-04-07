from django.db import models

sex_choices = (
    ('male', 'Male'),
    ('female', 'Female')
)

role_choices = (
    ('student', 'Student'),
    ('teacher', 'Teacher')
)


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, choices=sex_choices)
    country = models.CharField(max_length=128, null=True)
    role = models.CharField(max_length=32, choices=role_choices, null=True)
    avatar = models.ImageField(upload_to='student_pics', blank=True)

    def __str__(self):
        return self.name
