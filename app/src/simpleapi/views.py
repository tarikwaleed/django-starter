from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class SimpleView(APIView):
    def get(self, request, *args, **kwargs):
        # query_param = request.GET.get("param")
        # body_param = request.data.get("body_param")
        return Response("Hello, World", status=200)
