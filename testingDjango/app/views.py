from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'menu.html', context)
    

def element(request, element_id):
    if element_id is not None:
        print(element_id)
        return JsonResponse({ "id" : element_id })
    else:
        return JsonResponse({ "id" : 'None' })