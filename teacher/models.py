from django.db import models


class Professeur(models.Model):
    #id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    description = models.TextField()
    site_perso = models.URLField(max_length=80, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    google_url = models.CharField(max_length=255, null=True, blank=True)
    mail = models.EmailField()
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'professeur'