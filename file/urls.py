from django.urls import path

from . import views

app_name = "file"
urlpatterns = [
    path("list/", views.BucketView.as_view(), name="list"),
]
