import os
import django
from random import choice
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Techera.settings')
django.setup()

# from TecheraAPP.models import Usuario, Perfil, BlogPost
from datetime import date


fake = Faker()

def create_users_profiles_blogposts():

    for i in range(3):
        # Create Usuario
        usuario = Usuario(nombre=fake.name(), email=fake.email(), password=fake.password())
        usuario.save()

        # Create BlogPosts
        for j in range(5):
            titulo = fake.sentence(nb_words=3)
            descripcion = fake.paragraph(nb_sentences=2)
            fecha_creado = fake.date_between(start_date='-1y', end_date='today')

            blogpost = BlogPost(usuario=usuario, titulo=titulo, descripcion=descripcion, fecha_creado=fecha_creado)
            blogpost.save()

    print('Data added successfully!')

if __name__ == '__main__':
    create_users_profiles_blogposts()
