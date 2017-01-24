from django.contrib import admin
from .models import QuizzTitre, Quizz


class QuizzAdmin(admin.StackedInline):
    model = Quizz


class QuizzTitreAdmin(admin.ModelAdmin):
    inlines = [
        QuizzAdmin,
    ]


admin.site.register(QuizzTitre, QuizzTitreAdmin)
# admin.site.register(Quizz)
