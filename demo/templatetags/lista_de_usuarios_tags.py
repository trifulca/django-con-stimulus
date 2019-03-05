from django import template
import time
from django.contrib.auth.models import User
from django.core.paginator import Paginator


register = template.Library()

@register.inclusion_tag('tags/lista_de_usuarios.html')
def lista_de_usuarios(logo=""):
    time.sleep(12)
    usuarios = User.objects.all()

    paginator = Paginator(usuarios, 5)
    print(paginator)

    return {"usuarios": paginator.page(1)}
