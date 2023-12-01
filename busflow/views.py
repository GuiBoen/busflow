from django.shortcuts import render
import numpy as np

# Create your views here.
from django.http import HttpResponse
from .temp_data import busflow_data

def detail_ponto(request, ponto_id):
    context = {'ponto': busflow_data[ponto_id - 1]}
    return render(request, 'busflow/detail.html', context)

def list_pontos(request):
    context = {"pontos_list": busflow_data}  #a ver
    return render(request, 'busflow/index.html', context)

def search_pontos(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "pontos_list": [
                m for m in busflow_data
                if request.GET['query'].lower() in m['nome'].lower()
            ]
        }
    return render(request, 'busflow/search.html', context)

list_lotacao=np.zeros(26)

def mediaLotacao(request):
    ponto_id = request.POST.get('busflow_id')
    list_lotacao[ponto_id].append(request.POST['lotacao'])
    media = sum(list_lotacao) / float(len(list_lotacao))
    return round(media)
    

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