from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import Truncator

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
    list_display = ["titulo", "atual", "letreiro"]
    list_filter = ["titulo", "letreiro"]
    search_fields = ["titulo", "letreiro"]
    readonly_fields = ("visualizar_imagem",)

    fieldsets = [
        ("Tema", {"fields": ("titulo", "atual", ("foto", "visualizar_imagem"))}),
        ("Assunto", {"fields": ("redes_sociais",)}),
    ]

    def visualizar_imagem(self, obj):
        if obj.foto:  # Certifique-se de que o campo existe e contém um valor
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px;" />',
                obj.foto.url,
            )
        return "Sem imagem"

    visualizar_imagem.short_description = "Imagem Salva"


@admin.register(RedeSocial)
class RedeSocial(admin.ModelAdmin):
    list_display = ["nome", "icone", "link"]
    list_filter = ["nome"]
    search_fields = ["home", "nome"]


@admin.register(Apresentacao)
class Apresentacao(admin.ModelAdmin):
    list_display = ["titulo", "atual", "foto", "texto"]
    list_filter = ["titulo"]
    search_fields = [
        "titulo",
    ]
    readonly_fields = ("visualizar_imagem",)

    fieldsets = [
        (
            "Tema",
            {"fields": ("titulo", "atual", ("foto", "visualizar_imagem"), "texto")},
        ),
        ("Assunto", {"fields": ("sub_titulo", "sub_texto")}),
    ]

    def visualizar_imagem(self, obj):
        if obj.foto:  # Certifique-se de que o campo existe e contém um valor
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px;" />',
                obj.foto.url,
            )
        return "Sem imagem"

    visualizar_imagem.short_description = "Imagem Salva"


@admin.register(Abordagem)
class Abordagem(admin.ModelAdmin):
    list_display = ("titulo", "atual", "texto")
    list_filter = ["titulo"]
    search_fields = [
        "titulo",
    ]
    fieldsets = [
        ("Tema", {"fields": ("titulo", "atual", "texto")}),
    ]


@admin.register(IndicesAbordagem)
class IndicesAbordagemAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "abordagem",
        "format_data",
        "exibindo",
        "data_publicacao",
    )
    list_filter = ["titulo"]
    search_fields = [
        "titulo",
    ]
    readonly_fields = ("format_data",)
    fieldsets = [
        ("Assunto", {"fields": ("abordagem", "titulo")}),
        (
            "Controle",
            {
                "fields": (
                    "format_data",
                    ("exibindo", "data_publicacao"),
                )
            },
        ),
    ]

    def format_data(self, obj):
        if obj.data:
            return obj.data.strftime("%d/%m/%Y")
        return "—"

    format_data.short_description = "Criado"


@admin.register(TextosIndiceAbordagem)
class TextosIndiceAbordagem(admin.ModelAdmin):
    list_display = (
        "indice",
        "sub_titulo",
        "sub_texto_truncado",
        "format_data",
        "exibindo",
        "data_publicacao",
    )
    list_filter = ["indice"]
    search_fields = [
        "indice",
    ]
    readonly_fields = ("format_data",)
    fieldsets = [
        ("Assunto", {"fields": ("indice", "sub_titulo", "sub_texto")}),
        (
            "Controle",
            {
                "fields": (
                    "format_data",
                    ("exibindo", "data_publicacao"),
                )
            },
        ),
    ]

    def format_data(self, obj):
        if obj.data:
            return obj.data.strftime("%d/%m/%Y")
        return "—"

    format_data.short_description = "Criado"

    def sub_texto_truncado(self, obj):
        return Truncator(obj.sub_texto).chars(50)  # Limita a 50 caracteres

    sub_texto_truncado.short_description = "Texto"  # Título da coluna


@admin.register(GrupoExperiencia)
class GrupoExperienciaAdmin(admin.ModelAdmin): ...


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["titulo", "grupo", "exibindo", "experiencia"]


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
        "exibindo",
        "data_publicacao",
    )
    fieldsets = [
        ("Assunto", {"fields": ("topico", "sub_titulo", "sub_texto")}),
        ("Controle", {"fields": ("data", "exibindo", "data_publicacao")}),
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
