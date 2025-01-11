from django import template
from datetime import date, datetime
from django.db.models import Max
from django.shortcuts import get_object_or_404
from collections import defaultdict


from dados.models import (
    Home,
    Apresentacao,
    TextosIndiceAbordagem,
    Experiencia,
    Card,
    Topico,
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
        indice__abordagem__atual=True, data_publicacao__lte=hoje
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
    experiencia = Experiencia.objects.filter(atual=True)
    data_desejada = datetime.now()
    # filtra os objetos exibindos com data de publicação maior ou igual à hoje
    card = Card.objects.filter(
        exibindo=True,
        data_publicacao__isnull=False,
        data_publicacao__lte=data_desejada,
    )

    # Filtra o ID mais recente de cada grupo onde exibindo é True
    latest_ids = (
        Card.objects.filter(
            exibindo=True,
            data_publicacao__isnull=False,
            data_publicacao__lte=data_desejada,
        )
        .values("grupo")
        .annotate(latest_id=Max("id"))
        .values_list("latest_id", flat=True)
    )

    # Filtra os grupos associados aos IDs mais recentes obtidos acima
    grupos = Card.objects.filter(id__in=latest_ids).values("grupo__nome").distinct()

    context = {
        "experiencia": experiencia,
        "grupos": grupos,
        "card": card,
    }
    return context


@register.inclusion_tag("includes/cardExperiencia.html")
def show_card_experiencia(card_id):
    data_desejada = datetime.now()

    # Use get_object_or_404 para pegar um único objeto
    card = get_object_or_404(
        Card,
        id=card_id,
        exibindo=True,
        data_publicacao__isnull=False,
        data_publicacao__lte=data_desejada,
    )

    context = {"card": card}  # card agora é um único objeto
    return context


@register.inclusion_tag("includes/topicos.html")
def show_topicos():
    topicos = Topico.objects.filter(atual=True)
    hoje = date.today()

    # Filtra os sub-tópicos
    subtopicos = SubTopico.objects.filter(
        exibindo=True, data_publicacao__lte=hoje
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


@register.inclusion_tag("includes/footer.html")
def show_footer():
    return
