from django.shortcuts import render
from django.template import Context, loader
from backoffice.models import Promotion, Event, Personne
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def evenements(request):
    event_list = Event.object.all()
    return render(request, 'evenements.html', {'event_list': event_list})

@login_required
def photos(request):
    return render(request, 'photos.html')

@login_required
def profil(request):
    return render(request, 'profil.html')

@login_required
def promo(request):
    promo_list = Promotion.object.all()
    return render(request, 'promotions.html', {'promo_list': promo_list})

@login_required
def trombi(request):
    perso_list = Personne.object.all()
    return render(request, 'trombinoscope.html', {'perso_list': perso_list})
