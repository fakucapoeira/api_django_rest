from django.db import models
from datetime import datetime   

# Create your models here.
class Project(models.Model):
    titulo= models.CharField(default='titulo1',max_length=250)
    descripcion= models.TextField(default='dd')
    tecnologia= models.CharField(default='',max_length=200)
    creado= models.DateTimeField(default=datetime.now(), blank=True)