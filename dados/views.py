from django.shortcuts import get_object_or_404, render

from dados.models import Card, Endereco, Email, Home, SubTopico, Telefone


# Create your views here.
def index(request):
    template_name = "index.html"
    endereco = Endereco.objects.all().last()
    email = Email.objects.all().last()
    telefone = Telefone.objects.all().last()
    context = {"endereco": endereco, "email": email, "telefone": telefone}
    return render(request, template_name, context)


def get_card_experience(request, card_id):
    template_name = "includes/cardExperiencia.html"
    data = Home.objects.all()
    card = get_object_or_404(Card, id=card_id)
    context = {"data": data, "card": card}
    return render(request, template_name, context)


def get_sub_topicos(request, subtop_id):
    template_name = "includes/subTopicos.html"
    data = Home.objects.all()
    subtop = get_object_or_404(SubTopico, id=subtop_id)
    context = {"data": data, "subtop": subtop}
    return render(request, template_name, context)