from django.db import models

# Create your models here.

class log(models.Model):
        zaman=models.DateField(auto_now=True)
        logip=models.CharField(max_length=500)

class uye(models.Model):
        adi=models.CharField(max_length=50, blank=True)
        soyadi=models.CharField(max_length=50, blank=True)
        bolumu=models.CharField(max_length=200, blank=True)
        eposta=models.EmailField(max_length=50, blank=True)
        parola=models.CharField(max_length=50, blank=True)