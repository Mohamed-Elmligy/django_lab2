
from django.contrib import admin
from django.urls import path, re_path
from .views import index, create,showAll,showOne,update,delete,edit
app_name = 'todo'

urlpatterns = [
    
    path('create/', create, name='create'),
    path('list/', showAll, name='list'),
    path('show/<int:item_id>/<str:item_name>', showOne, name='show'),
    path('edit/<int:task_id>', edit, name='edit'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
    path('', index, name='todo-index'),
]
