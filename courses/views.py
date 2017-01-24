from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Cour as c

# Create your views here.
def ListCours(request):
    perso = c.objects.all()
    template = loader.get_template('cours/c_list.html')
    context = {
        'perso' : perso
    }

    return HttpResponse(template.render(context, request))

def UnitCours(request, Cour_id):
    perso = c.objects.get(pk=Cour_id)
    return render(request, 'student/eleve.html', {
        'pid': Cour_id,
        'all': perso,
    })

