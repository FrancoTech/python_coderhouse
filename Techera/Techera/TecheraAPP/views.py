import json
from django.shortcuts import render, redirect
from datetime import date
from .models import  Perfil, BlogPost,Mensaje, About    
from django.contrib.auth.models import User
from .forms import UsuarioFormulario, PerfilFormulario, BlogPostFormulario, BuscaBlogPostForm, ElegirUsuarioForm, MensajeForm
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView, LogoutView
from django.db.models import Q



# Create your views here.

# def inicio(request):
#     return render(request, "TecheraAPP/index.html")


def usuarioFormulario(request):
    if request.method == "POST":
        formulario = UsuarioFormulario(request.POST) # Aqui me llega la informacion del html
        if formulario.is_valid():
            formulario.save()
            return redirect('Inicio')
    else:
        formulario = UsuarioFormulario()

    return render(request, "TecheraAPP/usuario-formulario.html", {"formulario": formulario})

def loginUsuario(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                django_login(request, user)
                return redirect('Inicio')
            else:
                return render(request, "TecheraAPP/login.html", {"mensaje":"Datos incorrectos"})

    formulario = AuthenticationForm()
    return render(request, 'TecheraAPP/login.html', {'formulario':formulario})

@login_required
def perfilFormulario(request):
    usuario = request.user
    perfil, _ =Perfil.objects.get_or_create(usuario=usuario)
    if request.method == "POST":
        formulario = PerfilFormulario(request.POST, request.FILES) # Aqui me llega la informacion del html
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            if informacion.get('descripcion'):
                perfil.descripcion = informacion["descripcion"]
            if informacion.get('nombre'):
                perfil.nombre = informacion["nombre"]
            if informacion.get('apellido'):
                perfil.apellido = informacion["apellido"]
            if informacion.get('edad'):
                perfil.edad = informacion["edad"]
            if informacion.get('website'):
                perfil.website = informacion["website"]
            perfil.avatar = informacion.get('avatar') or perfil.avatar
            if informacion.get('email'):
                usuario.email = informacion["email"]
            
            usuario.save()
            perfil.save()
            return render(request, "TecheraAPP/perfil-formulario.html", {"formulario":formulario})
        else:
            return render(request, "TecheraAPP/perfil-formulario.html", {"formulario":formulario})
    formulario = PerfilFormulario(        
        initial={
        'email':usuario.email,
        'descripcion':perfil.descripcion,
        'nombre':perfil.nombre,
        'apellido':perfil.apellido,
        'edad':perfil.edad,
        'website':perfil.website,
    })

    return render(request, "TecheraAPP/perfil-formulario.html", {"formulario": formulario, "perfil":perfil})

@login_required
def blogPostFormulario(request, id = None):
    
    if id: 
        blogPost = BlogPost.objects.get(id = id)    
        formulario = BlogPostFormulario(
            initial={
                'titulo':blogPost.titulo,
                'subTitulo':blogPost.subTitulo,
                'contenido':blogPost.contenido})
    else:
        blogPost = BlogPost(usuario=request.user)
        formulario = BlogPostFormulario()

    
    if request.method == "POST":
        formulario = BlogPostFormulario(request.POST, request.FILES) 
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            if informacion.get('titulo'):
                blogPost.titulo=informacion["titulo"]
            if informacion.get('subTitulo'):
                blogPost.subTitulo=informacion["subTitulo"]
            if informacion.get('contenido'):
                blogPost.contenido=informacion["contenido"]
            blogPost.imagen = informacion.get('imagen') or blogPost.imagen
            if blogPost.fecha_creado == None:
                blogPost.fecha_creado= date.today()
            blogPost.save()
            blogPosts = BlogPost.objects.all().order_by('-fecha_creado')
            return render(request, "TecheraAPP/index.html", {"formulario": BuscaBlogPostForm(),"blog_posts": blogPosts})

    return render(request, "TecheraAPP/blog-formulario.html", {"formulario": formulario})



def blogPostDetalle(request, id = None):
    if id: 
        blogPost = BlogPost.objects.get(id = id)    
        return render(request, "TecheraAPP/blog-post.html", {"blog_post": blogPost})
    else:
        blogPosts = BlogPost.objects.all().order_by('-fecha_creado')
        return render(request, "TecheraAPP/index.html", {"formulario": BuscaBlogPostForm(),"blog_posts": blogPosts})
        
@login_required
def blogEliminatPost(request, id = None):
    
    if id: 
        blogPost = BlogPost.objects.get(id = id)    
        
    blogPost.delete()

    blogPosts = BlogPost.objects.all().order_by('-fecha_creado')
    return render(request, "TecheraAPP/index.html", {"formulario": BuscaBlogPostForm(),"blog_posts": blogPosts})


def inicio(request):
    if request.method == "POST":
        formulario = BuscaBlogPostForm(request.POST) # Aqui me llega la informacion del html

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            blogPosts = BlogPost.objects.filter(contenido__contains=informacion["palabra"]).order_by('-fecha_creado')
            return render(request, "TecheraAPP/index.html", {"formulario": BuscaBlogPostForm(), "blog_posts": blogPosts})
    else:
        blogPosts = BlogPost.objects.all().order_by('-fecha_creado')
        formulario = BuscaBlogPostForm()
        
    return render(request, "TecheraAPP/index.html", {"formulario": formulario, "blog_posts": blogPosts})

@login_required
def mensajesView(request):
    if request.method == 'POST':
        print("entro aca 0")
        print(request)
        if 'boton_elegir_usuario' in request.POST:
            print("entro aca 1")

            elegir_usuario = ElegirUsuarioForm(request.POST)
            if elegir_usuario.is_valid():
                print("entro aca 2")
                info_usuario = elegir_usuario.cleaned_data
                destinatarioUser = info_usuario['usuario']
                mensajes = Mensaje.objects.filter(
                                                    Q(remitente=request.user, destinatario=destinatarioUser) |
                                                    Q(remitente=destinatarioUser, destinatario=request.user)
                                                )
                return render(request, "TecheraAPP/messages.html", {"elegir_usuario": ElegirUsuarioForm(initial={'usuario':destinatarioUser}), "enviar_mensaje": MensajeForm(), "destinatario": destinatarioUser, "mensajes":mensajes})
            else:
                print(elegir_usuario.errors)
        elif 'boton_enviar_mensaje' in request.POST:
            print("entro aca 11")
            enviar_mensaje = MensajeForm(request.POST)
            if enviar_mensaje.is_valid() :
                print("entro aca 12")
                info_mensaje = enviar_mensaje.cleaned_data
                if request.POST.get('destinatario_id'):
                    print("entro aca 13")
                    destinatarioUser = User.objects.get(id = request.POST.get('destinatario_id'))  
                    mensaje = Mensaje(destinatario=destinatarioUser, remitente = request.user)
                    if(info_mensaje.get('titulo')):
                        mensaje.titulo = info_mensaje.get('titulo')
                    if(info_mensaje.get('mensaje')):
                        mensaje.mensaje = info_mensaje.get('mensaje')
                    mensaje.save()
                # Procesa los datos del formulario dos
                # ...
                mensajes = Mensaje.objects.filter(
                                Q(remitente=request.user, destinatario=destinatarioUser) |
                                Q(remitente=destinatarioUser, destinatario=request.user)
                            )
                return render(request, "TecheraAPP/messages.html", {"elegir_usuario": ElegirUsuarioForm(initial={'usuario':destinatarioUser}), "enviar_mensaje": MensajeForm(), "destinatario": destinatarioUser, "mensajes":mensajes})
    else:
        elegir_usuario = ElegirUsuarioForm()
        enviar_mensaje = MensajeForm()

    return render(request, 'TecheraAPP/messages.html', {
        'elegir_usuario': elegir_usuario,
        'enviar_mensaje': enviar_mensaje,
    })
            

def aboutView(request):
    about = About.objects.get(id = 1)    
    return render(request, "TecheraAPP/about.html", {'about': about})

class Logout(LogoutView):
    template_name = 'TecheraAPP/logout-usuario.html'

