from django.shortcuts import render
from datetime import date
from .models import Usuario, Perfil, BlogPost
from .forms import UsuarioFormulario, PerfilFormulario, BlogPostFormulario, BuscaBlogPostForm



# Create your views here.

# def inicio(request):
#     return render(request, "TecheraAPP/index.html")


def usuarioFormulario(request):
    if request.method == "POST":
        formulario = UsuarioFormulario(request.POST) # Aqui me llega la informacion del html
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = Usuario(nombre=informacion["nombre"], email=informacion["email"], password=informacion["password"])
            usuario.fecha_creado = date.today()
            usuario.save()
            return render(request, "TecheraAPP/index.html")
    else:
        formulario = UsuarioFormulario()

    return render(request, "TecheraAPP/usuario-formulario.html", {"formulario": formulario})


def perfilFormulario(request):
    if request.method == "POST":
        formulario = PerfilFormulario(request.POST) # Aqui me llega la informacion del html
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            perfil = Perfil(usuario=informacion["usuario"], descripcion=informacion["descripcion"], edad=informacion["edad"])
            perfil.save()
            return render(request, "TecheraAPP/index.html")
    else:
        formulario = PerfilFormulario()

    return render(request, "TecheraAPP/perfil-formulario.html", {"formulario": formulario})


def blogPostFormulario(request):
    if request.method == "POST":
        formulario = BlogPostFormulario(request.POST) 
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = formulario.cleaned_data["usuario"]
            blogPost = BlogPost(titulo=informacion["titulo"], descripcion=informacion["descripcion"], usuario = usuario,fecha_creado = date.today() )
            blogPost.save()
            return render(request, "TecheraAPP/index.html")
    else:
        formulario = BlogPostFormulario()

    return render(request, "TecheraAPP/blog-formulario.html", {"formulario": formulario})

def inicio(request):
    if request.method == "POST":
        formulario = BuscaBlogPostForm(request.POST) # Aqui me llega la informacion del html

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            blogPosts = BlogPost.objects.select_related('usuario').filter(descripcion__contains=informacion["palabra"])
            return render(request, "TecheraAPP/index.html", {"formulario": BuscaBlogPostForm(), "blog_posts": blogPosts})
    else:
        blogPosts = BlogPost.objects.select_related('usuario').all()
        formulario = BuscaBlogPostForm()
        
    return render(request, "TecheraAPP/index.html", {"formulario": formulario, "blog_posts": blogPosts})

