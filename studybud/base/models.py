from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  # blank=True means it is not mandatory in forms
    # participants = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)  # auto_now=True means it will be updated every time the object is updated
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add=True means it will be added only once when the
                                                       # object is created
    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # connects the message to the user cascade means if the user is deleted then all the messages will be deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # connects the message to the room cascade means if the room is deleted then all the messages will be deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]  # this will return the first 50 characters of the message body