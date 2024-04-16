from django.shortcuts import render
from django.http import JsonResponse
from .models import Element

# Create your views here.
def home(request):
    # Получаем все элементы
    elements = Element.objects.all()

    # Создаем дерево элементов
    element_tree = []
    for element in elements:
        if element.parent is None:  # Если элемент является корневым
            element_tree.append(get_element_tree_dict(element, 1))

    context = {
        'element_tree_data': element_tree,
        'active_element_id': 1,
    }

    return render(request, 'menu.html', context)
    

def element(request, element_id):
    # Получаем все элементы
    elements = Element.objects.all()

    # Создаем дерево элементов
    element_tree = []
    for element in elements:
        if element.parent is None:  # Если элемент является корневым
            element_tree.append(get_element_tree_dict(element, element_id))

    context = {
        'element_tree_data': element_tree,
        'active_element_id': element_id,
    }

    return render(request, 'menu.html', context)
        

def get_element_tree_dict(element : Element, active_id : int, level=0):
    tree = {
        'id': element.id,
        'name': element.name,
        'active': element.id == active_id,
        'children': []
    }
    for child in element.children.all():
        child_tree = get_element_tree_dict(child, active_id, level + 1)
        tree['children'].append(child_tree)
    return tree
    