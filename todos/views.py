from django.shortcuts import render
from todos.models import TodoItem, TodoList
# Create your views here.


def show_todolists(request):
    model = TodoList.objects.all()
    return render(
        request,
        template_name="todolists/list.html",
        context={"todolists": model},
    )


def show_todoitems(request):
    model = TodoItem.objects.all()
    return render(
        request,
        template_name="todoitems/list.html",
        context={"todoitems": model},
    )
