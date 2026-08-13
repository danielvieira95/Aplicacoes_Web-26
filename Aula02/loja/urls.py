from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter

from produtos.views import ProdutoViewSet


def home(request):
    return HttpResponse("Olá Django! Aplicações Web 2026-2 - Aula 02 - Loja de Produtos")


router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]