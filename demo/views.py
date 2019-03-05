from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator

import time
import random


def index(request):
    return render(request, "index.html")

def about(request):
    time.sleep(1)

    valores = {
        "tiempo": random.randint(0, 99999)
    }

    valores['tiempo'] = 'tiempo: ' + str(valores['tiempo'])

    return render(request, "about.html", valores)

def usuarios(request):
    time.sleep(2)
    usuarios = User.objects.all()
    paginator = Paginator(usuarios, 5)

    valores = {"usuarios": paginator.page(1)}
    return render(request, "tags/lista_de_usuarios.html", valores)
