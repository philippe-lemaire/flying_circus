from django.urls import path

from . import views

app_name = "classes"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index_classes"),
    path(
        "<slug:course_slug>/<slug:slug>/",
        views.LessonDetailView.as_view(),
        name="lesson_detail",
    ),
]
