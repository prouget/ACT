from django.db import models
from django.core.validators import RegexValidator
from courses.models import Cour


class QuizzTitre(models.Model):
    titre_quizz = models.CharField(max_length=255)

    def __str__(self):
        return self.titre_quizz

    class Meta:
        db_table = 'titre_quizz'


class Quizz(models.Model):
    cour_ref = models.ForeignKey(Cour, null=True, blank=True)
    quizz_titre = models.ForeignKey(QuizzTitre, null=True, blank=True, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    numero_quizz = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    a = models.CharField(max_length=255, null=True)
    a_vrai = models.BooleanField(default=False)
    b = models.CharField(max_length=255, null=True)
    b_vrai = models.BooleanField(default=False)
    c = models.CharField(max_length=255, null=True)
    c_vrai = models.BooleanField(default=False)
    d = models.CharField(max_length=255, null=True)
    d_vrai = models.BooleanField(default=False)
    e = models.CharField(max_length=255, null=True)
    e_vrai = models.BooleanField(default=False)

    def __str__(self):
        return self.numero_quizz + ' -  ' + self.question

    class Meta:
        db_table = 'quizz'
        verbose_name = 'Questionnaire'
