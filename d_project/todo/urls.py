from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_todos,name='all-todos'),
    path('create-todo/',views.create_todo,name='create-todo'),
    path('mark-as-completed/<int:pk>/',views.mark_as_completed,name='mark-as-completed'),
]