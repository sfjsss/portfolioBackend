from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Project, Message
from .serializers import ProjectSerializer, MessageSerializer

# Create your views here.
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MessageViewSet(viewsets.ViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail = False, methods = ['POST'])
    def create_message(self, request):
        message = Message.objects.create(name = request.data['name'], email = request.data['email'], message = request.data['message'])
        serializer = MessageSerializer(message, many = False)
        response = {'message': 'message created', 'result': serializer.data}
        return Response(response, status = status.HTTP_200_OK)
