from django.contrib import admin
from django.urls import path, include
from backoffice import views
from TPCESI import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


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
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)