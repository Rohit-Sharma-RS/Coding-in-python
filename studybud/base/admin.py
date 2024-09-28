from django.contrib import admin

# Register your models here.
from .models import Room, Message, Topic

admin.site.register(Topic)
admin.site.register(Room)  # this will add Room model to the admin panel
admin.site.register(Message)
