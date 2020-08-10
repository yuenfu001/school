from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=20, help_text="enter your Surname here")
    first_name = models.CharField(max_length=20, help_text="enter your name here")
    courses = models.ManyToManyField("course", blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Meta:
    verbose_name_plural = "People"
    ordering = ["last_name", "first_name"]

class Course(models.Model):
    name = models.CharField(max_length=20, help_text="enter name of course here")
    year = models.TextField()
    def __str__(self):
        return f"{self.name}"


class Meta:
    unique_together = ("name", "year",)

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person} {self.course} {self.grade}"