from django.shortcuts import render


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
    return render(request, 'promotions.html')


def trombi(request):
    return render(request, 'trombinoscope.html')
