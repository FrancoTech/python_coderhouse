from django.urls import path
from TecheraAPP import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('usuario-formulario/', views.usuarioFormulario, name="Crear Usuario"),
    path('perfil-formulario/', views.perfilFormulario, name="Definir Perfil"),
    path('blog-formulario/', views.blogPostFormulario, name="Crear Blog"),
    path('blog-formulario/<id>/', views.blogPostFormulario, name="Editar Blog"),
    path('blog-post/<id>/', views.blogPostDetalle, name="Ver Blog"),
    path('accounts/login/?next=/blog-post/<id>/', views.blogPostDetalle, name="Ver Blog Not Logged"),
    path('login/', views.loginUsuario, name="Iniciar Sesion"),
    path('logout-usuario', views.Logout.as_view(), name='Logout'),
    path('blog-eliminar/<id>/', views.blogEliminatPost, name="Eliminar Blog"),
    path('messages', views.mensajesView,name="Messages"),
    path('about', views.aboutView,name="About"),

    
]