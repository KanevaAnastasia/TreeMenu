from django import template
from django.http import HttpRequest, request


from menu.models import Item, Menu

register = template.Library()

"""
Класс для определания пути до пункта меню
Путь реализован по типу односвязного списка
"""
class Path():
    def __init__(self, item, next):
        self.item = item
        self.next = next



@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, name):
    """
    Создаем включающий тэг для отрисовки меню
    """

    """
    Получаем все записи нужного меню за один запрос
    """
    data = Menu.objects.get(name=name)
    data = data.item_set.all()

    """
    Будем хранить все данные в нужных нам словарях:
    parent_child для хранения детей, принадлежащих каждому пункту меню
    child_parent для хранения родителя каждого пункта меню
    url_id для хранения id всех пунктов меню, соответствующих их url
    id_url для хранения каждого url соответствующих каждому пункту меню по id
    child_name - хранит имя для кажого id пунктов меню.
    Словари позваляют избежать лишние проходы по элементам меню
    """
    parent_child = dict()
    child_parent = dict()
    url_id = dict()
    id_url = dict()
    child_name = dict()

    """
    При проходе по всем записям базы данных заполняем словари
    """
    for i in data:
        parent = i.parent_id
        if parent != None:
            parent_child[parent.id] = parent_child.get(parent.id, [])
            parent_child[parent.id].append(i.id)
            child_parent[i.id] = parent.id
        else:
            parent_child[0] =  parent_child.get(0, [])
            parent_child[0].append(i.id)
            child_parent[i.id] = 0
        url_id[i.url] = i.id
        id_url[i.id] = i.url
        child_name[i.id] = i.name

    """
    Определяем, есть ли в данном меню выбранный пункт меню
    """
    child = url_id.get(context['url'], 0)

    """
    Определяем путь до выбранного пункта меню
    """
    i = child
    path = None
    while i != 0:
        path = Path(i, path)
        i = child_parent[i]

    """
    Отрисовка меню начитается с нулевого уровня
    """
    start = 0


    return {'start': start, 'path': path, 'parent_child': parent_child,
            'child_name':child_name, 'url':context['url'], 'id_url':id_url, 'child':child}












