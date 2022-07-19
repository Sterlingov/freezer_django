from django.shortcuts import render, get_object_or_404
from .models import MainModel


def freezers(request):
    freezers_model = MainModel.objects.order_by('-price')
    return render(request, "base.html", {"freezers_model": freezers_model})


def item_detail(request, pk):
    items = get_object_or_404(MainModel, pk=pk)
    return render(request, "item_detail.html", {"items": items})
