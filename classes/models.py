from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=100)
    levels = [
        ("1", "Débutant"),
        ("2", "Intermédiaire"),
        ("3", "Avancé"),
    ]
    level = models.CharField(max_length=1, choices=levels, default="1")
    order = models.IntegerField(default=1)
    content = HTMLField()
    manager = models.OneToOneField(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=100)
    order = models.IntegerField(default=1)
    content = HTMLField()
    manager = models.OneToOneField(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title
