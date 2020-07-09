from django.urls import path , include
from .views import views as main_view
from .views import menu_views as menu_view

menupatterns = [
    path('add/', menu_view.add),
    path('', menu_view.index, name='manage_menu_index'),
    path(r'^edit/', menu_view.edit_menu_item, name='manage_menu_edit'),
]

urlpatterns = [
    path('', main_view.index),
    path('menu/', include(menupatterns)),
]
