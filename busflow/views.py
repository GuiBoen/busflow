from django.shortcuts import render, get_object_or_404
from .models import pontos, onibus, usuario, horario32
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .temp_data import busflow_data
from django.views import generic
from datetime import datetime, timedelta

class PontosListView(generic.ListView):
    model = pontos
    template_name = 'busflow/index.html'

horarios32 = horario32.objects.all()
lista_horarios = []
for j in horarios32:
    lista_horarios.append(j.horario)

def calctempo(tempo_proximo):
    aux=lista_horarios[0]
    hora_atual = datetime.now()
    for i in lista_horarios:
        aux = datetime.combine(datetime.today(), aux)
        proximo = aux + timedelta(minutes=tempo_proximo)
        diferenca = hora_atual - timedelta(hours=proximo.hour, minutes=proximo.minute) 
        if diferenca.hour < hora_atual.hour or ((diferenca.hour == hora_atual.hour) and (diferenca.minute < hora_atual.minute)): 
            return diferenca 
        aux = i
         
def fazvetor(v):
    n=[]
    for i in v:       
        if i.isdigit():
            n.append(int(i))
    return n


def tempo(ponto, bus):
    listapontos = fazvetor(bus.id_linha.List_id_pontos)
    indice = listapontos.index(ponto.id)
    tempo_proximo = indice * 5
    print('\n', tempo_proximo, '\n')
    return calctempo(tempo_proximo)
    

def detail_ponto(request, ponto_id):
    ponto = get_object_or_404(pontos, pk=ponto_id)
    bus = get_object_or_404(onibus, pk=3)
    time = tempo(ponto,bus)
    context = {"ponto": ponto, "bus": bus, "time": time}
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

list_lotacao = []
t=len(pontos.objects.all())
for i in range(t):
    list_lotacao.append([])
def mediaLotacao(lot, ponto_id):
    list_lotacao[ponto_id].append(int(lot))
    media = sum(list_lotacao[ponto_id]) / len(list_lotacao[ponto_id])
    return round(media)

@login_required
def update_ponto(request, ponto_id):
    ponto = get_object_or_404(pontos, pk=ponto_id)
    if request.method == "POST":
        media = mediaLotacao(request.POST['lotacao'], ponto_id)
        ponto.lotacao = media
        ponto.save()
        return HttpResponseRedirect(
            reverse("busflow:detail", args=(ponto.id, )))
    
    context = {'ponto': ponto}
    return render(request, 'busflow/update.html', context)

@login_required
def import_ponto(request):
    if request.method == 'POST':
        ponto_id = request.POST['ponto_id']
    return render(request, 'busflow/import.html', {})

list_lotacao_onibus=[]
l = len(onibus.objects.all())
for j in range(l):
    list_lotacao_onibus.append([])

def mediaLotacao_Onibus(lot_onibus, onibus_id):
    list_lotacao[onibus_id].append(int(lot_onibus))
    media_onibus = sum(list_lotacao[onibus_id]) / len(list_lotacao[onibus_id])
    return round(media_onibus)

@login_required
def update_onibus(request, onibus_id):
    bus = get_object_or_404(onibus, pk=onibus_id)

    if request.method == "POST":
        media = mediaLotacao_Onibus(request.POST['lotacao'], onibus_id)
        bus.lotacao = media
        bus.save()
        return HttpResponseRedirect(
            reverse("busflow:detail_onibus", args=(bus.id, )))
    
    context = {'bus': bus}
    return render(request, 'busflow/update_onibus.html', context)    

def detail_onibus(request, onibus_id):
    bus = get_object_or_404(onibus, pk=onibus_id)
    context = {"bus": bus}
    return render(request, "busflow/detail_onibus.html", context)


