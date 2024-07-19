from django.urls import path

from . import views

app_name = "file"
urlpatterns = [
    path("list/", views.BucketListView.as_view(), name="list"),
    path("delete/<str:pk>", views.BucketDeleteView.as_view(), name="delete"),
]
