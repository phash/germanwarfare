from django.db import models
from django.utils import timezone

# Create your models here.

class Munition(models.Model):
    id = models.AutoField(primary_key=True)
    bezeichnung = models.CharField(max_length=200)
    schadenmin = models.IntegerField()
    schadenmax = models.IntegerField()
    durchschlag = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return"%s" %(self.bezeichnung)

class Waffe(models.Model):
    id = models.AutoField(primary_key=True)
    bezeichnung = models.CharField(max_length=200)
    dpm = models.IntegerField()
    aimtime = models.FloatField()
    reloadtime = models.FloatField()
    munition = models.IntegerField()
    genauigkeit = models.FloatField()
    munitionen = models.ManyToManyField(Munition)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return"%s" %(self.bezeichnung)

class Art(models.Model):
    id = models.AutoField(primary_key=True)
    bezeichnung = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return"%s" %(self.bezeichnung)

class Fahrzeug(models.Model):
    id = models.AutoField(primary_key=True)
    bezeichnung = models.CharField(max_length=200)
    art = models.ForeignKey(Art)
    tier_choices = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8')
    )
    tier = models.IntegerField(choices=tier_choices, default =1)
    ruhm = models.IntegerField()
    kosten = models.IntegerField()
    besatzung = models.IntegerField()
    turmdrehen = models.IntegerField()
    hitpoints = models.IntegerField()
    topgeschwindigkeit = models.FloatField()
    beschleunigung = models.FloatField()
    sichtweite = models.IntegerField()
    wanneFront = models.IntegerField()
    wanneSeite  = models.IntegerField()
    wanneHeck  = models.IntegerField()
    turmFront = models.IntegerField()
    turmSeite = models.IntegerField()
    turmHeck = models.IntegerField()
    waffen = models.ManyToManyField(Waffe)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return"%s" %(self.bezeichnung)

