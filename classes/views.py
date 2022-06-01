from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, Lesson

# Create your views here.


class IndexView(ListView):
    model = Course
    ordering = "order"
