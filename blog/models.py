from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255) ## cria corretamente a coluna no bd como varchar
    slug = models.SlugField(max_length=255, unique=True) ##texto da url, ex: /blog/introducao-django (letras, numeros, hifen)
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## Cada post tem um author e um autor pode ter mais de um post, on_delete é oq ocorre ao deletar o autor, cascade deleta todos post do autor
    body = models.TextField() # corpo do post, nao tem tamanho minimo
    created = models.DateTimeField(auto_now_add=True) #data de cruacao adicionada auto
    updated = models.DateTimeField(auto_now=True) #data da ultima modificacao automaticamente

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug}) ##dicionario keywordsargs, serve para definir a url de um post

