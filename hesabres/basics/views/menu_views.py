from django.shortcuts import render
from basics.forms import addMenuForm
from basics.models import Menu
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.core.serializers import serialize
import json
# Add function in menu views
# _ is for the translation
def add(request):
    if request.method == "POST":
        form = addMenuForm(request.POST)
        if form.is_valid():
            addItem = Menu(name=request.POST['name'], price=request.POST['price'])
            addItem.save()
            messages.success(request, _('The item successfully added to menu.'))

    else :
        form = addMenuForm()

    return render(request, 'menu/add.html', {'form': form})





def index(request):
    data = Menu.objects.all()
    form = addMenuForm()
    return render(request, 'menu/index.html', {'data':data, 'edit_form': form})


# This function has bug 
def edit_menu_item(request):
    id = request.POST['item_id']
    item = Menu.objects.get(pk=id)
    item = '{"name": %s, "price": %s}'.format(item.name, item.price)
    asJson = json.dumps(item)   
    edit_item_data = serialize('json', [asJson])
    return JsonResponse(asJson, safe=False)
