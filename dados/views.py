from django.shortcuts import render

from dados.models import Endereco, Email, Telefone


# Create your views here.
def index(request):
    template_name = "index.html"
    endereco = Endereco.objects.all().last()
    email = Email.objects.all().last()
    telefone = Telefone.objects.all().last()
    context = {"endereco": endereco, "email": email, "telefone": telefone}
    return render(request, template_name, context)
