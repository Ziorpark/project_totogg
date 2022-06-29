from django.db import models
from django.utils.timezone import now

# Create your models here.
class GameSaver(models.Model):
    
    teamName = models.CharField(max_length=100)
    name = models.CharField(max_length=100) # 중복을 허용하지않기 
    rst = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    champ = models.CharField(max_length=200)  
    kda = models.CharField(max_length=200)
    ratio = models.CharField(max_length=200)
    pkill = models.CharField(max_length=200)
    cs = models.CharField(max_length=200)
    gtime = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.name}--{self.rst}--{self.created_at}"