from django.shortcuts import render
from django.contrib.auth.models import User

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
    valores = {"usuarios": usuarios}
    return render(request, "tags/lista_de_usuarios.html", valores)
