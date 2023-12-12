from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu_template.html')
def draw_menu(menu_name, request):

    if menu_name == "main_menu":
        menu_items = MenuItem.objects.filter(parent=None)
        return {'request': request, 'menu_items': menu_items}
