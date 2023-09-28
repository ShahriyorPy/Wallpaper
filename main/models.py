from django.db import models

# Create your models here.

class MyPhoto(models.Model):
    title = models.CharField(max_length=30, verbose_name="nomi")
    image = models.URLField(verbose_name="rasmning url'i")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="yuklangan sana",null=True,blank=True)

    def __str__(self):
        return self.title