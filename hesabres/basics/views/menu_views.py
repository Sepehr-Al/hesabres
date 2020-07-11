from django.shortcuts import render, HttpResponse, redirect
from basics.forms import addMenuForm
from django import shortcuts
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
    if request.method == 'POST':
        id = request.POST.get('item_id')
        #item = Menu.objects.get(pk=id)
        item = shortcuts.get_object_or_404(Menu, pk=id)
        edit_item_data = serialize('json', [ item ] )
        return JsonResponse(edit_item_data, safe=False)
    else :
        return redirect('manage_menu_index')







