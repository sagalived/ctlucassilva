from django.contrib import admin
from .models import MediaGaleria  # <-- MUDANÇA AQUI: de ImagemGaleria para MediaGaleria

# Registra o novo modelo para aparecer no painel administrativo
admin.site.register(MediaGaleria)