from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    other_details = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    course_description = models.TextField()
    other_details = models.TextField()

    def __str__(self):
        return self.course_name
