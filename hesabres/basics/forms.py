from django.forms import ModelForm
from basics.models import Menu
from django.utils.translation import gettext as _

# Form for adding data to the menu database
class addMenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price', ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class' : 'form-control',
            'id' : 'validationTooltip01',
            'placeholder' : _('American Pizza'),
            'required' : 'true',
            'name' : 'name',
        })

        self.fields['price'].widget.attrs.update({
            'class' : 'form-control',
            'required' : 'true',
            'placeholder' : _('10.9$'),
            'name' : 'price',
        })

