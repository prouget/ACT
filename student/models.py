from django.db import models


class Etudiant(models.Model):
    #id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    description = models.TextField()
    mail = models.EmailField()
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.nom) + ' ' + str(self.prenom)

    class Meta:
        db_table = 'étudiant'


