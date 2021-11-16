
# from django.contrib import admin
from django.urls import path, re_path
from .views import movie_index, movie_create,movie_detail,movie_update,movie_delete
app_name = 'movie'
urlpatterns = [
    path('create/', movie_create, name='create'),
    path('show-one/<int:item_id>', movie_detail, name='show'),
    # path('edit/<int:item_id>', edit, name='edit-item'),
    path('update/<int:item_id>', movie_update, name='update'),
    path('delete/<int:item_id>', movie_delete, name='delete'),
    path('',movie_index, name='index'),
]
