from django.contrib import admin


from .forms import HomeForm
from .models import (
    Endereco,
    Email,
    GrupoExperiencia,
    Experiencia,
    Card,
    Telefone,
    Home,
    RedeSocial,
    Apresentacao,
    Abordagem,
    IndicesAbordagem,
    TextosIndiceAbordagem,
    Topico,
    SubTopico,
)


@admin.register(Endereco)
class Endereco(admin.ModelAdmin): ...


@admin.register(Email)
class Email(admin.ModelAdmin): ...


@admin.register(Telefone)
class Telefone(admin.ModelAdmin): ...


@admin.register(Home)
class Home(admin.ModelAdmin):
    form = HomeForm
    list_display = ["titulo", "letreiro"]
    list_filter = ["titulo", "letreiro"]
    search_fields = ["titulo", "letreiro"]
    readonly_fields = ("visualizar_imagem",)

    def visualizar_imagem(self, obj):
        return obj.view_image

    visualizar_imagem.allow_tags = True
    visualizar_imagem.short_description = "Imagem Cadastrada"


@admin.register(RedeSocial)
class RedeSocial(admin.ModelAdmin):
    list_display = ["nome", "icone", "link"]
    list_filter = ["nome"]
    search_fields = ["home", "nome"]


@admin.register(Apresentacao)
class Apresentacao(admin.ModelAdmin):
    list_display = ["titulo", "foto", "texto"]
    list_filter = ["titulo"]
    search_fields = [
        "titulo",
    ]
    readonly_fields = ("visualizar_imagem",)

    def visualizar_imagem(self, obj):
        return obj.view_image

    visualizar_imagem.allow_tags = True
    visualizar_imagem.short_description = "Imagem Cadastrada"


@admin.register(TextosIndiceAbordagem)
class TextosIndiceAbordagem(admin.ModelAdmin):
    list_display = (
        "indice",
        "sub_titulo",
        "sub_texto",
        "data",
        "publicado",
        "data_publicacao",
    )
    fieldsets = [
        ("Assunto", {"fields": ("indice", "sub_titulo", "sub_texto")}),
        ("Controle", {"fields": ("data", "publicado", "data_publicacao")}),
    ]


@admin.register(IndicesAbordagem)
class IndicesAbordagem(admin.ModelAdmin):
    list_display = (
        "titulo",
        "abordagem",
        "data",
        "publicado",
        "data_publicacao",
    )


@admin.register(Abordagem)
class Abordagem(admin.ModelAdmin):
    list_display = ("titulo", "texto")


@admin.register(GrupoExperiencia)
class GrupoExperienciaAdmin(admin.ModelAdmin): ...


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["titulo", "grupo", "publicado", "experiencia"]


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = [
        "titulo",
        "texto",
    ]


@admin.register(SubTopico)
class SubTopico(admin.ModelAdmin):
    list_display = (
        "topico",
        "sub_titulo",
        "sub_texto",
        "data",
        "publicado",
        "data_publicacao",
    )
    fieldsets = [
        ("Assunto", {"fields": ("topico", "sub_titulo", "sub_texto")}),
        ("Controle", {"fields": ("data", "publicado", "data_publicacao")}),
    ]


@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    list_display = [
        "titulo",
        "texto",
    ]
    fieldsets = [
        ("Assunto", {"fields": ("titulo", "texto")}),
    ]
    list_filter = ["titulo"]
    search_fields = ["titulo"]
    ordering = ("titulo",)
