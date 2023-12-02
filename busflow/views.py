from django.shortcuts import render, get_object_or_404
import numpy as np
from .models import pontos, onibus, usuario

from django.http import HttpResponse
from .temp_data import busflow_data
from django.views import generic

class PontosListView(generic.ListView):
    model = pontos
    template_name = 'busflow/index.html'

def detail_ponto(request, ponto_id):
    ponto = get_object_or_404(pontos, pk=ponto_id)
    context = {"ponto": ponto}
    return render(request, "busflow/detail.html", context)

def list_pontos(request):
    pontos_list = pontos.objects.all()
    context = {"pontos_list": pontos_list}
    return render(request, "busflow/index.html", context)


def list_onibus(request):
    onibus_list = onibus.objects.all()
    context = {"onibus_list": onibus_list}
    return render(request, "busflow/index.html", context)


def list_usuarios(request):
    usuario_list = usuario.objects.all()
    context = {"usuario_list": usuario_list}
    return render(request, "busflow/index.html", context)

# def list_pontos(request):
#     ponto_list
#     context = {"pontos_list": busflow_data}  #a ver
#     return render(request, 'busflow/index.html', context)


def search_pontos(request):
    context = {}
    if request.GET.get("query", False):
        search_term = request.GET['query'].lower()
        pontos_list = pontos.objects.filter(nome__icontains=search_term)
        context = {"pontos_list": pontos_list}
    return render(request, "busflow/search.html", context)


# list_lotacao = np.zeros(26)


# def mediaLotacao(request, ponto_id):
#     list_lotacao[ponto_id].append(request.POST["lotacao"])
#     media = sum(list_lotacao[ponto_id]) / float(len(list_lotacao[ponto_id]))
#     return round(media)


# def modify_lotacao(request):
#     if request.method == 'UPDATE':
#         media=mediaLotacao(request)
#         busflow_data.append({
#             'lotacao': request.POST.set[media],
#             })
#         return HttpResponseRedirect(
#             reverse('movies:detail', args=(len(movie_data), )))
#     else:
#         return render(request, 'movies/create.html', {})

def update_ponto(request, ponto_id):
    ponto = get_object_or_404(pontos, pk=ponto_id)

    if request.method == "POST":
        # ponto.lotacao = request.POST['mediaLotacao(request, ponto_id)']
        ponto.lotacao = request.POST['lotacao']
        ponto.save()
        return HttpResponseRedirect(
            reverse("busflow:detail", args=(ponto.id )))
    
    context = {'ponto': ponto}
    return render(request, 'busflow/update.html', context)