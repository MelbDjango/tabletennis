from django.shortcuts import render
from .models import Tournament


def home(request):
    tournament = Tournament.objects.latest()
    
    return render(request, 'tournament.html', {
        'tournament': tournament,
    })
