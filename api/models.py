from django.db import models

# Create your models here.
class Project(models.Model):
    projectName = models.CharField(max_length = 32)
    summary = models.TextField(max_length = 360)
    bgImage = models.TextField(max_length = 360)
    source_code = models.TextField(max_length = 360, blank = True)

    def __str__(self):
        return self.projectName

class Stack(models.Model):
    name = models.CharField(max_length = 32)
    projects = models.ManyToManyField(Project, related_name = 'stacks')

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length = 32, blank = False)
    email = models.CharField(max_length = 64, blank = False)
    message = models.TextField(max_length = 360, blank = False)

    def __str__(self):
        return self.name