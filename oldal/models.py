from django.db import models

# Create your models here.

class Oldal(models.Model):
    hatter = models.FileField(upload_to="static/images")


class Cimek(models.Model):
    cim = models.CharField(max_length=200)






    def __str__(self):
        return self.cim
