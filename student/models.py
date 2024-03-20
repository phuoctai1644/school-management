from django.db import models


class Student(models.Model):
    sex_choices = (
        ('Male', 'male'),
        ('Female', 'female')
    )

    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, choices=sex_choices)
    avatar = models.ImageField(upload_to='student_pics')

    def __str__(self):
        return self.name
