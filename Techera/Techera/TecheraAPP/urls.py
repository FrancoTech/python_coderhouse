from django.urls import path
from TecheraAPP import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('usuario-formulario/', views.usuarioFormulario, name="Crear Usuario"),
    path('perfil-formulario/', views.perfilFormulario, name="Definir Perfil"),
    path('blog-formulario/', views.blogPostFormulario, name="Crear Blog"),

    
]