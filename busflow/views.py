from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .temp_data import busflow_data

def detail_ponto(request, ponto_id):
    ponto = busflow_data[ponto_id - 1]
    return HttpResponse(
        f'Detalhes do ponto {ponto["name"]} ({ponto["lotacao"]})')