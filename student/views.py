from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Etudiant as e

# Create your views here.

def index(request):
    return render(request, 'Index.html') 

def ListStudent(request):
    perso = e.objects.all()
    template = loader.get_template('student/liste.html')
    context = {
        'perso' : perso
    }

    return HttpResponse(template.render(context, request))

def UnitStudent(request, Etudiant_id):
    perso = e.objects.get(pk=Etudiant_id)
    return render(request, 'student/eleve.html', {
        'pid': Etudiant_id,
        'e': perso,
    })