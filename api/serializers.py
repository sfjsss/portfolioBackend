from rest_framework import serializers
from .models import Project, Stack, Message

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ('name',)

class ProjectSerializer(serializers.ModelSerializer):
    stacks = StackSerializer(many = True)

    class Meta:
        model = Project
        fields = ('id', 'projectName', 'summary', 'bgImage', 'stacks', 'source_code')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'name', 'email', 'message')