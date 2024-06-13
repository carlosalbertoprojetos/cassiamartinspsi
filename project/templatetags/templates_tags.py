from django import template
from datetime import date

from dados.models import (
    Home,
    Apresentacao,
    IndiceAbordagem,
    Abordagem,
    Indice,
    Topico,
    SubTopico,
)

register = template.Library()


@register.inclusion_tag("includes/header.html")
def show_header():
    data = Home.objects.all()
    context = {"data": data}
    return context


@register.inclusion_tag("includes/apresentacao.html")
def show_apresentacao():
    data = Apresentacao.objects.all()
    context = {"data": data}
    return context


@register.inclusion_tag("includes/abordagem.html")
def show_abordagem():
    abordagem = Abordagem.objects.all()
    indice = Indice.objects.all()
    indice_abordagem = IndiceAbordagem.objects.all()
    context = {
        "abordagem": abordagem,
        "indice": indice,
        "indice_abordagem": indice_abordagem,
    }
    return context


@register.inclusion_tag("includes/topicos.html")
def show_topicos():
    topicos = Topico.objects.all()
    hoje = date.today()

    # Filtra os sub-tópicos
    subtopicos = SubTopico.objects.filter(
        publicado=True, data_publicacao__lte=hoje
    ).order_by("-data_publicacao")[:6]

    icones = [
        "bi bi-briefcase",
        "bi bi-card-checklist",
        "bi bi-bar-chart",
        "bi bi-binoculars",
        "bi bi-brightness-high",
        "bi bi-calendar4-week",
    ]

    # Associar ícones aos subtopicos
    for i, subtopico in enumerate(subtopicos):
        subtopico.icone = icones[i % len(icones)]  # Usar ícones de forma cíclica

    context = {"topicos": topicos, "subtopicos": subtopicos}
    return context


@register.inclusion_tag("includes/.html")
def show_():

    pass


@register.inclusion_tag("includes/.html")
def show_():

    pass


@register.inclusion_tag("includes/footer.html")
def show_footer():
    return
