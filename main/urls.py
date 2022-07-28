from django.urls import URLPattern, path
from . import views
from .models import ToDoList, Item
urlpatterns = [
    

    path('', views.home, name='home'),
    path('<int:id>', views.index, name='index'),
    path('<str:name>', views.index, name='index'),
    path('create/', views.create, name='create'),

    

]