# in mygame/web/story.py
from django.shortcuts import render

def webclient(request):
    return render(request, "new_webclient.html")
