from django.contrib import admin
from .models import BlogPost, Perfil, Mensaje, About

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Perfil)
admin.site.register(Mensaje)
admin.site.register(About)