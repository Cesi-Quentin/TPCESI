from django.db import models


class Personnes(models.Model):
    nom = models.CharField(max_lenght=150)
    prenom = models.CharField(max_lenght=150)
    datenaissance = models.DateTimeField()
    adresse = models.TextField()
    tel = models.IntegerField()
    photo = models.TextField() #blob


class Intervenants(models.Model):
    entreprise = models.CharField(max_length=200)


class Eleves(models.Model):
    classeid = models.IntegerField()


class Promotion(models.Model):
    nom = models.CharField(max_length=50)


class Events(models.Model):
    nom = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateTimeField()
    lieu = models.TextField()


class Publication(models.Model):
    post = models.TextField()
    title = models.TextField()
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    object = models.Manager()

    def __unicode__(self):
        return self.title