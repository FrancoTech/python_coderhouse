from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


class UsuarioFormulario(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', help_text='Es necesario que sea menor a 150 caracteres')
    email = forms.EmailField(label='Correo', help_text='Es necesario que sea menor a 150 caracteres')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { key: '' for key in fields }

class PerfilFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Email')
    descripcion = forms.CharField(label='Descripcion')
    website = forms.CharField()
    avatar = forms.ImageField(required=False)


    
class BlogPostFormulario(forms.Form):
    titulo = forms.CharField(required=True)
    subTitulo = forms.CharField()
    contenido = forms.CharField(widget=CKEditorWidget(),required=True)
    imagen = forms.ImageField(required=True)
    
class BuscaBlogPostForm(forms.Form):
    palabra = forms.CharField()
    
class ElegirUsuarioForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.all())
    
class MensajeForm(forms.Form):
    titulo = forms.CharField(required=True)
    mensaje = forms.CharField(widget=CKEditorWidget(),required=True)