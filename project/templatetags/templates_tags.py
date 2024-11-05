from django import template
from datetime import date, datetime
from django.db.models import Max
from django.shortcuts import get_object_or_404


from dados.models import (
    Home,
    Apresentacao,
    Abordagem,
    IndicesAbordagem,
    TextosIndiceAbordagem,
    Experiencia,
    Card,
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
    indice = IndicesAbordagem.objects.all()
    indice_abordagem = TextosIndiceAbordagem.objects.all()
    context = {
        "abordagem": abordagem,
        "indice": indice,
        "indice_abordagem": indice_abordagem,
    }
    return context


@register.inclusion_tag("includes/experiencia.html")
def show_experiencia():
    experiencia = Experiencia.objects.all()
    data_desejada = datetime.now()
    # filtra os objetos publicados com data de publicação maior ou igual à hoje
    card = Card.objects.filter(
        publicado=True,
        data_publicacao__isnull=False,
        data_publicacao__lte=data_desejada,
    )

    # Filtra o ID mais recente de cada grupo onde publicado é True
    latest_ids = (
        Card.objects.filter(
            publicado=True,
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
        publicado=True,
        data_publicacao__isnull=False,
        data_publicacao__lte=data_desejada,
    )

    context = {"card": card}  # card agora é um único objeto
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


@register.inclusion_tag("includes/footer.html")
def show_footer():
    return
