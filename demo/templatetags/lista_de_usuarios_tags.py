from django import template
import time
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('tags/lista_de_usuarios.html')
def lista_de_usuarios(logo=""):
    time.sleep(2)
    usuarios = User.objects.all()
    return {"usuarios": usuarios}
