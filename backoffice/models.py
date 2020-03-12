from django.conf import settings
from django.db import models


class Promotion(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(null=True)
    object = models.Manager()

    def __unicode__(self):
        return self.nom


class Personne(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    datenaissance = models.DateTimeField()
    adresse = models.TextField()
    tel = models.IntegerField()
    photo = models.TextField() #blob
    statut = models.CharField(max_length=50)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    object = models.Manager()

    def __unicode__(self):
        return self.nom


class Event(models.Model):
    nom = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateTimeField()
    lieu = models.TextField()
    object = models.Manager()

    def __unicode__(self):
        return self.nom


class Publication(models.Model):
    post = models.TextField()
    title = models.TextField()
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    object = models.Manager()

    def __unicode__(self):
        return self.nom