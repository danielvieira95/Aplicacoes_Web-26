from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer

# Create your views here


from django.http import HttpResponse

def home(request): 
    return HttpResponse("Olá Django! Aplicações Web 2026-2 - Aula 02 - Loja de Produtos")
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by("-id")
    serializer_class = ProdutoSerializer