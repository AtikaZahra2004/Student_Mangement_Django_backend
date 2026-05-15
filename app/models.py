from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Course = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)

    def __str__(self):
        return self.Name