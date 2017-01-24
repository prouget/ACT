from django.db import models
from tinymce.models import HTMLField
from courses.models import Cour


class Leçon(models.Model):
    cour_ref = models.ForeignKey(Cour, null=True)
    nom = models.CharField(max_length=255, null=True)
    contenu = HTMLField()
    video_url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'lesson'
