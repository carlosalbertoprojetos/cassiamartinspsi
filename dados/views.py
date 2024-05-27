from django.shortcuts import render

# from dados.models import Elemento, Abordagem


# Create your views here.
def index(request):
    template_name = "index.html"
    # elemento = Elemento.objects.all()
    # abordagem = Abordagem.objects.all()
    # context = {"elemento": elemento, "abordagem": abordagem}
    context = {}
    return render(request, template_name, context)
