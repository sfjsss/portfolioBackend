from django.contrib import admin
from .models import Project, Stack, Message

# Register your models here.
admin.site.register(Project)
admin.site.register(Stack)
admin.site.register(Message)