from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Learn React'},
    {'id': 2, 'name': 'Learn Django'},
    {'id': 3, 'name': 'Learn HTML'},
]


# Create your views here.
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context = {'room': room}
    return render(request, 'base/room.html', context)
