from django.shortcuts import render
from rest_framework.views import APIView
from app1.models import Snippet
from app1.serializer import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class SnippetApi(APIView):

    

    def get(self, request, format=None):

        snippets = Snippet.objects.all()

        snippet_serializer = SnippetSerializer(snippets, many=True)

        return Response(snippet_serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, format=None):
        
        snippet_serializer = SnippetSerializer(data=request.data)

        if snippet_serializer.is_valid():

            snippet_serializer.save()

            return Response(snippet_serializer.data, status=200)
        return Response(snippet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        