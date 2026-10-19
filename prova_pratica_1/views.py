from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request,"prova_pratica_1/index.html")

def somma(request):
    context={'var1': random.randint(1,10), 'var2': random.randint(1,10)}

    return render(request,"prova_pratica_1/somma.html",context)

def media(request):
    voti=[]
    media=0
    count=0
    for i in range (30):
        voti.append(random.randint(1,10))
        media=media+voti[i]
        count+=1
    media=media/count
    
    return render(request,"prova_pratica_1/media.html",voti,media)

def voti(request):
    context={'studente1': 8, 'studente2':9, 'studente3':10}
    return render(request,"prova_pratica_1/voti.html",context)