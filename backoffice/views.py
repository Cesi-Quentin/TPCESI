from django.shortcuts import render
from django.template import Context, loader
from backoffice.models import Promotion
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def evenements(request):
    return render(request, 'evenements.html')


def photos(request):
    return render(request, 'photos.html')


def profil(request):
    return render(request, 'profil.html')


def promo(request):
    promo_list = Promotion.object.all()
    return render(request, 'promotions.html', {'promo_list': promo_list})


def trombi(request):
    return render(request, 'trombinoscope.html')
