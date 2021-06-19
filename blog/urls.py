from django.urls import path

from . import views

app_name = 'blog' ##variavel importante para referenciar as urls desse arquivo

#as_view para tornar callable
#name para referenciar e evitar conflito entre urls com msm nome

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]  ## lista de padroes de url, url sem argumentos vai na lista de post, com slug vai para pagina de um post