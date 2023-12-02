from django.contrib import admin

# Register your models here.
from .models import linhas, horario32, onibus, pontos, usuario

admin.site.register(linhas)
admin.site.register(horario32)
admin.site.register(onibus)
admin.site.register(pontos)
admin.site.register(usuario)