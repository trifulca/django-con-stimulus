from django import template
register = template.Library()

@register.inclusion_tag('tags/menu.html')
def menu(logo):
    return {"logo": logo}
    #return {"items": [1, 2, 3], "logo": logo}
