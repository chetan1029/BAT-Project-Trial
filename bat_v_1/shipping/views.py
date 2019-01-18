from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from shipping.models import (Shipment)
from shipping.forms import (ShipmentForm)
from django.db.models import Q
# Create your views here.
# 1. Shipment
 ## 1.1 Shipment
  ### 1.1.1 ShipmentListView
  ### 1.1.2 ShipmentDetailView
  ### 1.1.3 CreateShipmentView
  ### 1.1.4 ShipmentUpdateView
  ### 1.1.5 ShipmentDeleteView

# 1. Shipment
 ## 1.1 Shipment
  ### 1.1.1 ShipmentListView
class ShipmentListView(LoginRequiredMixin,ListView):
    model = Shipment
    template_name = 'shipment/shipment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment"}
        return context

  ### 1.1.2 ShipmentDetailView
class ShipmentDetailView(LoginRequiredMixin,DetailView):
    model = Shipment
    template_name = 'shipment/shipment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"detail"}
        return context

  ### 1.1.3 CreateShipmentView
class CreateShipmentView(LoginRequiredMixin,CreateView):
    form_class = ShipmentForm
    model = Shipment
    template_name = 'shipment/shipment_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment"}
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Products'))
        return context

  ### 1.1.4 ShipmentUpdateView
class ShipmentUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ShipmentForm
    model = Shipment
    template_name = 'shipment/shipment_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment"}
        return context

  ### 1.1.5 ShipmentDeleteView
class ShipmentDeleteView(LoginRequiredMixin,DeleteView):
    model = Shipment
    template_name = 'shipment/shipment_confirm_delete.html'
    success_url = reverse_lazy('shipping:shipment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment"}
        return context
