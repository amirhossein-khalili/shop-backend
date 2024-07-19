import asyncio

from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import tasks
from .tasks import all_bucket_objects_task


class BucketListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        result = tasks.all_bucket_objects_task()
        return Response({"bucket_items": result})


class BucketDeleteView(APIView):

    permission_classes = [IsAdminUser]

    def delete(self, request, key):

        tasks.delete_object_task.delay(key)

        return Response({"message": "your object will be delete soon."})


# class DownloadBucketObject(IsAdminUserMixin, View):
#     def get(self, request, key):
#         tasks.download_object_task.delay(key)
#         messages.success(request, "your download will start soon.", "info")
#         return redirect("home:bucket")
