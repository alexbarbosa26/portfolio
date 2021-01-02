from django.contrib import admin
from .models import Ativo, Cotacao, Nota, Proventos
# Register your models here.
admin.site.register(Nota)
admin.site.register(Cotacao)
admin.site.register(Proventos)
admin.site.register(Ativo)