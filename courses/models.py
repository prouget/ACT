from django.db import models
from tinymce.models import HTMLField



class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nom_categorie

    class Meta:
        db_table = 'catégorie'


class Cour(models.Model):
    nom_cour = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, null=True)
    description = HTMLField()

    def __str__(self):
        return self.nom_cour

    class Meta:
        db_table = 'cour'
