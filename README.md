## Referencia do estudo

Estudo do video: [https://www.youtube.com/watch?v=NZd386TfzcM](https://www.youtube.com/watch?v=NZd386TfzcM)

## Intro

Leitura: [https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Introduction](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Introduction)

## [O que é Django?](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Introduction#o_que_%C3%A9_django)

Django é um framework web Python de alto nível que permite o rápido desenvolvimento de sites seguros e de fácil manutenção. Construido por desenvolvedores experientes, o Django cuida de grande parte do trabalho de desenvolvimento web, para que você possa se concentrar em escrever seu aplicativo sem precisar reinventar a roda. É gratuito e de código aberto, tem uma comunidade próspera e ativa, ótima documentação e muitas opções de suporte gratuito e pago.

Django ajuda você a escrever programas que são:

**Completo**

Django segue a filosofia de "baterias incluídas" e fornece quase tudo que desenvolvedores possam querer fazer "fora da caixa". Como tudo o que você precisa é parte de um "produto", tudo funciona perfeitamente junto, seguindo princípios de design consistentes, contando uma extensa e [atualizada documentação](https://docs.djangoproject.com/pt-br/2.1/).

**Versátil**

Django pode ser (e tem sido) utilizado para construir quase todo tipo de website - desde sistema de gestão de conteúdo e wikis, passando por redes sociais e sites de notícias. Ele pode trabalhar com qualquer framework do lado do cliente, e pode entregar conteúdo em praticamente qualquer formato (incluindo HTML, feeds RSS, JSON, XML, etc). Esse site que você está lendo agora é baseado em Django.À medida em que, internamente, fornece opções para quase todo tipo de funcionalidade que você possa querer (por exemplo: vários banco de dados que são populares, motores de template, etc), ele pode também ser extendido para utilizar outros componentes, caso seja necessário.

**Seguro**

Django ajuda os desenvolvedores a evitar os erros de segurança mais comuns, fornecendo um framework que foi desenhado para "fazer as coisas certas", de modo a proteger o website automaticamente. Por exemplo, Django fornece uma maneira segura de gerenciar as contas dos usuários e suas senhas, evitando erros comuns, tais como colocar informações da sessão em cookies, onde ficam vulneráveis (ao invés disso os cookies contém apenas uma chave e os dados são armazenados no banco de dados), ou armazenar as senhas de forma direta, ao invés de gravar um hash para essas senhas.*Um hash de senha é um valor fixed-length (tamanho-fixo) criado mandando a senha por uma [cryptographic hash function (função hash criptográfica)](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_hash_criptogr%C3%A1fica). Django pode checar se uma senha inserida está correta executando ela pela função hash e comparando a saída com o valor hash armazenado. Porém devido a natureza "one-way" ("um-caminho") da função, mesmo que o valor hash armazenado estiver comprometido, é difcil para uma pessoa comentendo um ataque resolver a senha original.*O Django ativa a proteção contra muitas vulnerabilidades por padrão, incluindo SQL injection (injeção de SQL), cross-site scripting, cross-site request forgery (Falsificação de solicitação entre sites), e clickjacking ("furto de click") (veja [Segurança de sites](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Website_security) para mais detalhes de tais ataques).

**Escalável**

Django usa uma arquitetura baseada em componentes “[shared-nothing](https://en.wikipedia.org/wiki/Shared_nothing_architecture)” ("nada-compartilhado") (cada parte da arquitetura é idependente das outras, e consequentemente podem ser subistituidas ou mudadas caso necessário). Ter uma separação clara entre as partes diferentes significa que pode se escalar para um trágefo aumentado adicionando hardware em qualquer nível: servidores de cache, servidores de banco de dados ou servidores de aplicação. Alguns dos sites mais ocupados escalaram o Django com sucesso para cumprir com as suas demandas (ex: Instagram e Disqus).

**Sustentável**

O código do Django é escrito usando princípios de design e padrões que encorajam a criação de codigo sustentável (que facilita a manutenção) e reusável. Em particular, isso utiliza o principio  DRY - Don't Repeat Yourself (Não Repita a Si Mesmo) para que não haja duplicações desnecessárias, reduzindo a quantidade de código. O Django também promove o agrupamento de funcionalidades relacionadas para aplicativos reusáveis e, em um nível mais baixo, grupos de código relacionados para modulos (juntamente as linhas do padrão [MVC - Model View Controller](https://pt.wikipedia.org/wiki/MVC)).

**Portável**

Django é escrito em Python, que executa em muitas plataformas. Isso significa que você não esta preso em nenhuma plataforma de servidor em particular, e pode executar seus aplicativos em muitas distrubuições do Linux, Windows e Mac OS X. Além disso, o Django tem um bom suporte em muitos provedores de servidores de web, que muitas vezes provem infraestrutura especifca e documentação para hospedar sites feitos com Django.

## Agenda

- Como criar um projeto com o Django
- O que são e como criar apps
- O que são e como criar models
- O que são migrations e como trabalhar com elas
- Sobre a interface de admin do Django
- A usar a API para acessar o banco de dados
- O que é uma view
- Como conectar uma url a uma view
- O que são templates e como trabalhar com elas
- Como adicionar css no projeto.

```bash
python -m venv venv 
.\venv\Scripts\activate
pip install django
django-admin startproject tutorialdjango
cd tutorialdjango
code .
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b83754b-bdb8-405e-837b-8b984ea6c502/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b83754b-bdb8-405e-837b-8b984ea6c502/Untitled.png)

__init__.py :

- Tratar a pasta como um modulo python
- asgi.py:
- wsgi.py:
- settings.py:

    ```python
    Debug = True ## Detalha melhor os erros em ambiente de desenvolvimento

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',  ## interface de admins
        'django.contrib.auth', ## Cuida do sistema de autenticacao
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    # Projeto possui varios apps e um app pode estar em varios valores

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
    # Comumente usado postgres para producao
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    ```

- urls.py:

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python [manage.py](http://manage.py/) migrate' to apply them.

Qual esse erro?

Migrations são arquivos python responsaveis por gerenciar a estrutura no nosso banco de dados.

Solução?

aplicar as migrations

Comandos para detalhar todos os sqls que serão executados

```bash
python .\[manage.py](http://manage.py/) sqlmigrate auth 0001
```

```python
python .\[manage.py](http://manage.py/) sqlmigrate sessions 0001
```

para migrar, basta inserir p comando

```bash
python .\manage.py migrate
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d9c7d7d1-90ef-49b7-8926-10b17f0edfe4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d9c7d7d1-90ef-49b7-8926-10b17f0edfe4/Untitled.png)

para criar um app o comando é o seguinte:

```bash
python .\manage.py startapp blog
```

## Models

o que é um model?

- Fonte unica e definitiva de nossos dados, campos e comportamentos essenciais dos dados armazenados
- em codigo → classe python que herda a classe model do django, alguns atributos vao ser colunas/campos da tabela
- gera uma api automaticamente para acessar o bd, com um codigo python simples

touch ./blog/models.py

```python
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255) ## cria corretamente a coluna no bd como varchar
    slug = models.SlugField(max_length=255, unique=True) ##texto da url, ex: /blog/introducao-django (letras, numeros, hifen)
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## Cada post tem um author e um autor pode ter mais de um post, on_delete é oq ocorre ao deletar o autor, cascade deleta todos post do autor
    body = models.TextField() # corpo do post, nao tem tamanho minimo
    created = models.DateTimeField(auto_now_add=True) #data de cruacao adicionada auto
    updated = models.DateTimeField(auto_now=True) #data da ultima modificacao automaticamente
```

```bash
python .\[manage.py](http://manage.py/) makemigrations blog
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8e1625f4-d311-4f57-ae6d-017ab6d3c035/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8e1625f4-d311-4f57-ae6d-017ab6d3c035/Untitled.png)

normalmente o nome das tabelas seguem o seguinte padrão:

 app_module

```bash
python .\manage.py sqlmigrate blog 0001
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b38ad4c3-17b8-4962-83d8-d41de3b8dea4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b38ad4c3-17b8-4962-83d8-d41de3b8dea4/Untitled.png)

"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT → criado para dar um id unico para cada post

criar migration:

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f297c619-a04a-4c37-89f8-9733c172d061/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f297c619-a04a-4c37-89f8-9733c172d061/Untitled.png)

```bash
python .\[manage.py](http://manage.py/) createsuperuser
```

```bash
python .\[manage.py](http://manage.py/) runserver
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bc98cf4-0b4f-445e-8cca-094aa0d20c47/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bc98cf4-0b4f-445e-8cca-094aa0d20c47/Untitled.png)

como adicionar para criar posts pela interface?

editar arquivo admin.py

```python
from django.contrib import admin

from .models import Post

admin.site.register(Post)
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc5b9840-32a0-42b1-a242-5f3ae260254b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc5b9840-32a0-42b1-a242-5f3ae260254b/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/18fdfe6a-5dc2-41cc-a3a3-3fa77020fdba/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/18fdfe6a-5dc2-41cc-a3a3-3fa77020fdba/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ad110ea3-eb79-451d-b2d3-8a9643bf2645/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ad110ea3-eb79-451d-b2d3-8a9643bf2645/Untitled.png)

Como modificar o nome do post criado?

acessar models.py

```python
def __str__(self):
        return self.title
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f45f085e-095c-4cd3-8e2c-925362cf0160/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f45f085e-095c-4cd3-8e2c-925362cf0160/Untitled.png)

adicionando campos de descrição do post:

editar o admin.py

```python
from django.contrib import admin

from .models import Post

@admin.register(Post)  ##registra modelo na interface
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug","author", "created", "updated")
		prepopulated_fields = {"slug": ("title",)} ##preenche o slug em base ao titulo no novo post
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c594f8e6-82d0-48d7-8064-a86db0faf18b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c594f8e6-82d0-48d7-8064-a86db0faf18b/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/70fcb0aa-7272-41ce-bc10-5d451dc0d715/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/70fcb0aa-7272-41ce-bc10-5d451dc0d715/Untitled.png)

```bash
pip install ipython
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b234c54f-af55-43c4-83a8-704732904b09/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b234c54f-af55-43c4-83a8-704732904b09/Untitled.png)

Post.objects (método)

QuerySet ⇒ colecao de objetos de nosso bd (neste caso sao todos posts do blog)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd016374-d24e-446d-bbbf-6c0abc234661/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd016374-d24e-446d-bbbf-6c0abc234661/Untitled.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1b5261f0-ad5b-4ac9-9ea4-b67a3b73b10d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1b5261f0-ad5b-4ac9-9ea4-b67a3b73b10d/Untitled.png)

## Views

São funções do python que recebem request e retornam response, ex: html, json, excel, csv, etc.

criar por meio de funções e por meio de classes

views.py

```python
from django.views.generic import DetailView, ListView ## um lista 1 detalhado e outro lista todas views

from .models import Post

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
```

> Continuar em 57min —>[https://www.youtube.com/watch?v=Dzuiy-JNi-E](https://www.youtube.com/watch?v=Dzuiy-JNi-E)

edintando e inserindo as urls no blog (blog/urls.py):

```python
from django.urls import path

from . import views

app_name = 'blog' ##variavel importante para referenciar as urls desse arquivo

#as_view para tornar callable
#name para referenciar e evitar conflito entre urls com msm nome

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]  ## lista de padroes de url, url sem argumentos vai na lista de post, com slug vai para pagina de um post
```

validando essas urls no projeto (./urls.py)

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
] ## incluindo as urls do blog no projeto
```

```bash
python [manage.py](http://manage.py) runserver
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7a0b313-0398-4689-b48f-a631ea9e3f85/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7a0b313-0398-4689-b48f-a631ea9e3f85/Untitled.png)

com o debug=true vemos que com as 2 paginas configuradas não estamos vendo a pagina do foguete. acessando a pagina do blog:

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c26b63c0-1cd7-4f9b-b645-a6dd94d2098f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c26b63c0-1cd7-4f9b-b645-a6dd94d2098f/Untitled.png)

erro que não encontrou o post_list.html

(views genericas, precisam determinar um arquivo padrao de template)

Aqui configuramos quais dados devem ser exibidos para o usuario

## Templates

Definição de como os dados serão apresentados

*DTL e HTML time!*

```bash
touch blog/templates/blot/post_list.html
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d12d305d-f9f2-4346-8ee9-833c114efda4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d12d305d-f9f2-4346-8ee9-833c114efda4/Untitled.png)

Template tag: (base.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Fazin Walker</h1>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

{% block title %}{% endblock %} ⇒ Template Tag (importar os conteudos do django para o html)

```html
{% extends "blog/base.html" %}
```

```html
{% extends "blog/base.html" %}
<!-- herdar o formato da estrutura base.html -->
{% block title %}Meu blog Django/Python{% endblock %}
<!-- definir o title -->

{% block content %}
<!-- preencher o main -->
    {% for post in post_list %}
    <!-- varrer cada item do post_list -->
        <article>
            <h2>{{ post.title }}</h2>
            <p class="date">
                Publicado em: {{ post.created }} By {{ post.author }}
            </p>
            {{ post.body|linebreaks|truncatewords:10 }}
            <!-- pipes (filtros) para quebrar em linhas e nao mostrar todo texto -->
        </article>
    {% endfor %}
{% endblock %}
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/88862b0c-78ad-4b71-87f8-f15d7f6cfd9d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/88862b0c-78ad-4b71-87f8-f15d7f6cfd9d/Untitled.png)

```html
{% extends "blog/base.html" %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
    <h2>{{ post.title }}</h2>
    <p class="date">
        Publicado em {{ post.created }} por {{ post.author }}
    </p>
    {{ post.body|linebreaks }}

{% endblock %}
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/906db9d5-45a9-4687-82f6-428869971c46/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/906db9d5-45a9-4687-82f6-428869971c46/Untitled.png)

definindo a url dos posts (recursos)

```python
def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug}) ##dicionario keywordsargs, serve para definir a url de um post
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ecda4490-27c9-4a54-8c52-49931acfe900/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ecda4490-27c9-4a54-8c52-49931acfe900/Untitled.png)

editando no post_list para acessar pelo titulo cada um dos posts

```html
{% extends "blog/base.html" %}
<!-- herdar o formato da estrutura base.html -->
{% block title %}Meu blog Django/Python{% endblock %}
<!-- definir o title -->

{% block content %}
<!-- preencher o main -->
    {% for post in post_list %}
    <!-- varrer cada item do post_list -->
        <article>
            <h2>
                <a href="{{ post.get_absolute_url }}">
                    {{ post.title }}
                </a>
            </h2>
            <p class="date">
                Publicado em: {{ post.created }} By {{ post.author }}
            </p>
            {{ post.body|linebreaks|truncatewords:10 }}
            <!-- pipes (filtros) para quebrar em linhas e nao mostrar todo texto -->
        </article>
    {% endfor %}
{% endblock %}
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6b6be39-10e0-4ddb-a481-093ded4f5a0c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6b6be39-10e0-4ddb-a481-093ded4f5a0c/Untitled.png)

## Links:

Github:

[https://github.com/Fazin/django-tutorial](https://github.com/Fazin/django-tutorial)

Discord:

[https://discord.gg/3gb3zGZ](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnRjeG1XdHNKX3IzaExJOVo1N0RWb082V0JhZ3xBQ3Jtc0trZzlvdEQ1dElteVZvTjB1Zjk3UThXaGxLT3BNRkpZVm1YMW5XWUVhRHhqbXUyRk04MzhwS1FkeUo1S0xTWXd1YXRfWFZUVWpYYVoxVk9jRXNYdHVlVVVwUHVTeWFGVHlLYjZrVHJOQzNoMXRGYl8wUQ&q=https%3A%2F%2Fdiscord.gg%2F3gb3zGZ)

Documentação Django:

[https://docs.djangoproject.com/en/3.1/](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTliLWZ0R0w4NWFtdGNqVDlKc1JadElwU0hGQXxBQ3Jtc0tsWWxmT090Sk5HQ2lpUjNPekN3bTRka1hZTk5JN09VM1hJUFZkUmNLaGZtVnJLOWJvaU42enBLTWw2VlhYOUpOX2RRWlJ4NDk0WGZhYmh3SmtGb3lWT0dsOUVFSU9XYXpVSWxEZjVRR2JKN2xfLUc2UQ&q=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F3.1%2F)

Tutorial oficial Django:

[https://docs.djangoproject.com/pt-br/...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUNMUnkwb3FTVHBwT0hLUFNTSVlqZi1VNlMzZ3xBQ3Jtc0trYy1jYkQwUUNLNUp4eER6Q3FFUEpqTFpxSTdjT05XVkFDVldZZFRCVTRMdmIySFU1Ni1QQnkycWJ1RWJzNFE2NUV5S3NOZWxqek43US1xSkl6bFFYUHphTDJ4cFZ3bUhObnNNMWF2WU41dTZ1SEVSbw&q=https%3A%2F%2Fdocs.djangoproject.com%2Fpt-br%2F3.1%2Fintro%2Ftutorial01%2F)

Classy Class-Based Views:

[https://ccbv.co.uk/](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbE5XR0d5NGhqQW5Fd08zUzJZV3RFazY1MDljd3xBQ3Jtc0trR1RZRlY5eUlwblFTT19qSXdieDN5aXQtbThTaFlid2RGT3ItSl9Xd253N3Ztbk84bHhkcE5ucjdSYllNWEcwZ2p0ajJremN1THZxTzRkT2Q4WUVoYTFBb0xKWTBwZUExcDVWQWxMMU5xY3RYUHdCWQ&q=https%3A%2F%2Fccbv.co.uk%2F)

Repositório GitHub com o código da aula (branch aula-tutorial-django):

[https://github.com/fabioruicci/django...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbElWSHZHUnJvdnNsS0lIY1RUYUR3LWU1ZGlBQXxBQ3Jtc0tuMG9obGN0eGpuNlNmNzAyMGYwclhTUDVSU1NJaUFNb3JQdXpsdFYtNGdPc21mTFlMTC1Ld2swUEdUc1pnbTMtNXhGWFFSS05hSk5GSkpyeG1CbGYxSkg5cUpzb2pUdllZQ19aTnljQmliN2Z1dDNUWQ&q=https%3A%2F%2Fgithub.com%2Ffabioruicci%2Fdjango-tutorial-portugues-blog%2Ftree%2Faula-tutorial-django)

Apps de terceiros:

[https://djangopackages.org/](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2lnVkhLUVdaUG40UW5Tam5aTUpxUDZPQUo5d3xBQ3Jtc0tsb3RONUh3UmZFcmxUeXprT2dJOGpqaU1kQ2Z4d0JLbVExSmhPRi00WUc2YUMxVTAxUXdFakR3bGpTME1iM0I4QVdOYnpScXNTVFJtY1laVGlWTm5GZkpCWnJ3eXZlWGVpd2prOWJRSFNPOUJTRW92QQ&q=https%3A%2F%2Fdjangopackages.org%2F)

Django Rest Framework:

[https://www.django-rest-framework.org/](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbm9kZmhxbDVpOUNOUnVGaVIwc1hIeEVKM3ZOQXxBQ3Jtc0ttTWs1clI4NDNVaEIxWVpaUm4xaEtUNXdCSW5FVkVkSU41SldJTWRralVBZWZwMktYTmlHY1prZ1BoRHNSSHZxb1NxNFFpd0hKbXhiZVFhNXlTM3Y2enpZZE1wTG5UbGFOdGtCTGlnRzR1R2pQTno5UQ&q=https%3A%2F%2Fwww.django-rest-framework.org%2F)
