from django import template

from dados.models import Home, Apresentacao, IndiceAbordagem, Abordagem, Indice, Topico

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
    context = {
        "topicos": topicos,
    }
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
