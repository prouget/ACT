from django.db import models

# Create your models here.
class Badge(models.Model):
    nom = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='ImageImport')

    def __str__(self):
        return self.nom