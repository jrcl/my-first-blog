from django.contrib import admin

# Register your models here.

#incluimos el modelo
from .models import Post


#para hacerlo visible en la pagina del administrador,
#lo registramos
admin.site.register(Post)
