from django.contrib import admin
from .models import Categorie, Cour
from lessons.models import Leçon


class lessonAdmin(admin.StackedInline):
    model = Leçon


class courAdmin(admin.ModelAdmin):
    inlines = [
        lessonAdmin
    ]

admin.site.register(Categorie)
admin.site.register(Cour, courAdmin)