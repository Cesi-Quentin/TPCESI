from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from backoffice import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('photos/', views.photos, name="photos"),
    path('profil/', views.profil, name="profil"),
    path('promo/', views.promo, name="promo"),
    path('trombi/', views.trombi, name="trombi"),
    path('event/', views.evenements, name="event"),
    path('accounts/', include('django.contrib.auth.urls')),

]
