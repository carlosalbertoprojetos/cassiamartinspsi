from django.contrib import admin


from .forms import HomeForm


from .models import (
    Email,
    Telefone,
    Home,
    RedeSocial,
    Apresentacao,
    Abordagem,
    Indice,
    IndiceAbordagem,
    # Elemento,
    # Abordagem,
    # TituloBloco,
    # Experiencia,
    Topico,
    # Contato,
    # Mensagem,
)


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


class IndiceAbordagemInline(admin.TabularInline):
    model = IndiceAbordagem
    extra = 1


class IndiceInline(admin.TabularInline):
    model = Indice
    extra = 1


@admin.register(IndiceAbordagem)
class IndiceAbordagem(admin.ModelAdmin):
    list_display = (
        "indice",
        "sub_titulo",
        "sub_texto",
        "data",
        "publicado",
        "data_publicacao",
    )


@admin.register(Indice)
class Indice(admin.ModelAdmin):
    list_display = (
        "titulo",
        "abordagem",
        "data",
        "publicado",
        "data_publicacao",
    )
    # inlines = [IndiceAbordagemInline]


@admin.register(Abordagem)
class Abordagem(admin.ModelAdmin):
    list_display = ("titulo", "texto")
    # inlines = [IndiceInline]


# @admin.register(Elemento)
# class ElementoAdmin(admin.ModelAdmin):
#     list_display = ["grupo", "titulo", "texto"]
#     list_filter = ["grupo", "titulo"]
#     search_fields = ["grupo", "titulo", "texto"]
#     ordering = ("grupo",)


# @admin.register(Abordagem)
# class AbordagemAdmin(admin.ModelAdmin):
#     list_display = [
#         "elemento",
#         "titulo",
#         "texto",
#         "data",
#         "publicado",
#         "data_publicacao",
#     ]
#     fieldsets = [
#         ("Elemento da abordagem", {"fields": ("elemento",)}),
#         ("Tema", {"fields": ("titulo", "texto")}),
#         ("Registro", {"fields": ("data", "publicado", "data_publicacao")}),
#     ]
#     list_filter = [
#         "elemento",
#         "titulo",
#         "texto",
#         "data",
#         "publicado",
#         "data_publicacao",
#     ]
#     search_fields = ["elemento", "titulo", "data", "data_publicacao"]
#     ordering = ("elemento",)


# @admin.register(TituloBloco)
# class TituloBlocoAdmin(admin.ModelAdmin):
#     list_display = [
#         "grupo",
#         "titulo",
#     ]
#     list_filter = ["grupo", "titulo"]
#     search_fields = ["grupo", "titulo"]
#     ordering = ("grupo",)


# @admin.register(Experiencia)
# class ExperienciaAdmin(admin.ModelAdmin):
#     list_display = [
#         "titulo_bloco",
#         "imagem",
#         "texto",
#     ]
#     list_filter = ["titulo_bloco"]
#     search_fields = ["titulo_bloco"]


@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    list_display = [
        "titulo",
        "texto",
    ]
    fieldsets = [
        ("Assunto", {"fields": (("titulo", "texto"))}),
    ]
    list_filter = ["titulo"]
    search_fields = ["titulo"]
    ordering = ("titulo",)


# @admin.register(Contato)
# class ContatoAdmin(admin.ModelAdmin):
#     list_display = [
#         "localizacao",
#         "email",
#         "telefone",
#     ]


# @admin.register(Mensagem)
# class MensagemAdmin(admin.ModelAdmin):
#     # todos os campos ficam readonly
#     readonly_fields = [field.name for field in Mensagem._meta.fields]

#     list_display = [
#         "nome",
#         "email",
#         "titulo",
#         "texto",
#         "data",
#     ]
#     fieldsets = [
#         ("Identificação", {"fields": ("nome", "email")}),
#         ("Assunto", {"fields": (("titulo", "texto"))}),
#         (
#             "Registro",
#             {"fields": (("data",))},
#         ),
#     ]
#     list_filter = [
#         "nome",
#         "email",
#         "titulo",
#         "texto",
#         "data",
#     ]
#     search_fields = [
#         "nome",
#         "email",
#         "data",
#     ]
