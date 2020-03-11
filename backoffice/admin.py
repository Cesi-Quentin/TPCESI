from django.contrib import admin
from backoffice.models import Personne,Promotion,Event,Publication

# Register your models here.
admin.site.register(Personne)
admin.site.register(Promotion)
admin.site.register(Event)
admin.site.register(Publication)