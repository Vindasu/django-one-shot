from django.urls import path
from todos.views import (
    show_todoitems,
    show_todolists,
)

urlpatterns = [
    path("", show_todolists, name='list_todos'),
    path("", show_todoitems, name='item_todos')
]
