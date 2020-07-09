from django.shortcuts import render
from basics.forms import addMenuForm
from basics.models import Menu
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.core.serializers import serialize
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
    return render(request, 'menu/index.html', {'data':data})



def edit_menu_item(request):
    id = request.POST['item_id']
    # The below line has error !!!
    edit_item_data = serialize('json', Menu.objects.get(pk=id))
    return JsonResponse(edit_item_data, safe=False)
