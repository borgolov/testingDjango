from django.shortcuts import render
from django.http import JsonResponse
from .models import Element

# Create your views here.
def home(request):
    context = {}
    return render(request, 'menu.html', context)
    

def element(request, element_id):
    # Получаем все элементы
    elements = Element.objects.all()

    # Создаем дерево элементов
    element_tree = []
    for element in elements:
        if element.parent is None:  # Если элемент является корневым
            element_tree.extend(get_element_tree(element))

    # Вызываем функцию для печати дерева элементов
    print_element_tree(element_tree)

    return JsonResponse({'resp' : None})
        

def get_element_tree(element, level=0):
    tree = [[element]]  # Первый элемент - это сам элемент, остальные - дочерние
    for child in element.children.all():
        child_tree = get_element_tree(child, level + 1)
        tree[0].extend(child_tree)  # Добавляем дочерние элементы в список первого элемента
    return tree


def print_element_tree(tree, level=0):
    for item in tree:
        if isinstance(item, list):
            # Это список дочерних элементов, печатаем их рекурсивно
            print_element_tree(item, level + 1)
        else:
            # Это родительский элемент, печатаем его с отступами в зависимости от уровня
            print('  ' * level + item.name)
    