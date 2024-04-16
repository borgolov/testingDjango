from django import template

register = template.Library()

@register.simple_tag()
def draw_menu(element_tree, active_id=None):
    def is_ancestor(element, target_id):
        if element['id'] == target_id:
            return True
        for child in element.get('children', []):
            if is_ancestor(child, target_id):
                return True
        return False

    def draw_menu_recursive(element_tree, active_id):
        html = '<ul>'
        for element in element_tree:
            active_class = 'active' if element['id'] == active_id else ''

            if is_ancestor(element, active_id):
                html += f'<li><a class="{active_class}" href="/{element["id"]}">{element["name"]}</a>'
                if element['children']:
                    html += draw_menu_recursive(element['children'], active_id)
                html += '</li>'
            else:
                html += f'<li><a class="{active_class}" href="/{element["id"]}">{element["name"]}</a></li>'

        html += '</ul>'
        return html

    return draw_menu_recursive(element_tree, active_id)