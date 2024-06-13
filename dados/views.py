from django.shortcuts import render

from dados.models import Endereco, Email, Telefone, Topico, SubTopico


# Create your views here.
def index(request):
    template_name = "index.html"
    endereco = Endereco.objects.all().last()
    email = Email.objects.all().last()
    telefone = Telefone.objects.all().last()
    context = {"endereco": endereco, "email": email, "telefone": telefone}
    return render(request, template_name, context)


def topicos(request, id):
    template_name = "dados/topicos.html"
    topico = Topico.objects.all()
    subtopico = SubTopico.objects.all()

    context = {"topico": topico}

    return render(request, template_name, context)
