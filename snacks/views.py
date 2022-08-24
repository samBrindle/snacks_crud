from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


class ThingListView(ListView):
    template_name = "snack_list.html"
    model = Snack


class ThingDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class ThingCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["name","purchaser","description"]


class ThingUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["name", "description"]


class ThingDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")