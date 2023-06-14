from django import forms
from .models import Usuario


class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    email = forms.CharField(widget=forms.EmailInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class PerfilFormulario(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all())
    descripcion = forms.CharField(required=True)
    edad = forms.CharField(required=True)
    
class BlogPostFormulario(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), to_field_name='id')
    titulo = forms.CharField(required=True)
    descripcion = forms.CharField(required=True)
    
class BuscaBlogPostForm(forms.Form):
    palabra = forms.CharField()