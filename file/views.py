import asyncio

from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import tasks
from .tasks import all_bucket_objects_task


class BucketView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        result = tasks.all_bucket_objects_task()
        return Response({"bucket_items": result})
