from django.conf.urls import url, include
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # -- Cours ---
    url(r'^cours/$', views.ListCours, name='liste_cours'),
    url(r'^cours/(?P<Cours_id>[0-9]+)$', views.UnitCours, name='cours'),
]