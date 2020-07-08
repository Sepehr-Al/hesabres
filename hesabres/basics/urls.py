from django.urls import path , include
from .views import views as main_view
from .views import menu_views as menu_view

menupatterns = [
    path('add/', menu_view.add),
    path('', menu_view.index),
]

urlpatterns = [
    path('', main_view.index),
    path('menu/', include(menupatterns)),
]
