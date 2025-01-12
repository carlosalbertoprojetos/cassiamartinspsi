from django import template
from datetime import date
from django.db.models import Max
from django.shortcuts import get_object_or_404
from collections import defaultdict


from dados.models import (
    Home,
    Apresentacao,
    TextosIndiceAbordagem,
    Card,
    SubTopico,
)

register = template.Library()
hoje = date.today()


@register.inclusion_tag("includes/header.html")
def show_header():
    data = Home.objects.filter(atual=True)
    context = {"data": data}
    return context


@register.inclusion_tag("includes/apresentacao.html")
def show_apresentacao():
    data = Apresentacao.objects.filter(atual=True)
    context = {"data": data}
    return context


@register.inclusion_tag("includes/abordagem.html")
def show_abordagem():
    dados_organizados = defaultdict(lambda: defaultdict(list))

    abordagem_textos = {}  # Armazena os textos das abordagens

    # Obtém as abordagens, seus respectivos índices e conteúdos
    abordagens = TextosIndiceAbordagem.objects.filter(
        indice__abordagem__atual=True,
        indice__exibindo=True,
        indice__data_publicacao__lte=hoje,
        exibindo=True,
        data_publicacao__lte=hoje,
    )

    for item in abordagens:
        abordagem_titulo = item.indice.abordagem.titulo
        abordagem_textos = item.indice.abordagem.texto
        indice_titulo = item.indice.titulo

        # Organiza os itens em 'dados_organizados'
        dados_organizados[abordagem_titulo][indice_titulo].append(item)

    # Converte defaultdicts aninhados em dicionários simples
    dados_organizados = {
        abordagem: dict(indices) for abordagem, indices in dados_organizados.items()
    }

    context = {
        "dados_organizados": dados_organizados,
        "abordagem_textos": abordagem_textos,  # Inclui os textos das abordagens
    }
    return context


@register.inclusion_tag("includes/experiencia.html")
def show_experiencia():
    # Filtra os objetos exibindos com data de publicação maior ou igual à hoje
    card = Card.objects.filter(
        experiencia__atual=True,
        exibindo=True,
        data_publicacao__lte=hoje,
    )

    # Filtra o ID mais recente de cada grupo onde exibindo é True
    latest_ids = (
        card.values("grupo")
        .annotate(latest_id=Max("id"))
        .values_list("latest_id", flat=True)
    )

    # Filtra os grupos associados aos IDs mais recentes obtidos acima
    grupos = (
        Card.objects.filter(id__in=latest_ids, exibindo=True, data_publicacao__lte=hoje)
        .values("grupo__nome")
        .distinct()
    )

    context = {
        "experiencia": card,
        "grupos": grupos,
        "card": card,
    }
    return context


@register.inclusion_tag("includes/cardExperiencia.html")
def show_card_experiencia(card_id):
    # Usa o get_object_or_404 para pegar um único objeto
    card = get_object_or_404(
        Card,
        id=card_id,
        experiencia__atual=True,
        exibindo=True,
        data_publicacao__lte=hoje,
    )

    context = {"card": card}  # Card como único objeto
    return context


@register.inclusion_tag("includes/topicos.html")
def show_topicos():
    # Filtra os sub-tópicos
    subtopicos = SubTopico.objects.filter(
        topico__atual=True, exibindo=True, data_publicacao__lte=hoje
    ).order_by("-data_publicacao")[:6]

    # Filtra o título e o texto do tópico
    topico = subtopicos.values_list("topico__titulo", "topico__texto").first()

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

    context = {"topico": topico, "subtopicos": subtopicos}
    return context


@register.inclusion_tag("includes/footer.html")
def show_footer():
    return
