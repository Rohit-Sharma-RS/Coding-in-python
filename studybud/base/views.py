from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [
#     {'id':1, 'name':'Lets learn Django'},
#     {'id':2, 'name':'Lets learn Python'},
#     {'id':3, 'name':'Lets learn JavaScript'},
#     {'id':4, 'name':'Lets learn React'}
# ]


# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def create_room(request):
    context = {}
    return render(request, 'base/room_form.html',context=context)
