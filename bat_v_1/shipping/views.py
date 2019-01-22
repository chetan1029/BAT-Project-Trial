from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from shipping.models import (Shipment, ShipmentProduct)
from shipping.forms import (ShipmentForm, ShipmentProductForm)
from settings.models import (Status)
from suppliers.models import (OrderProduct)
from django.db.models import Q
# Create your views here.
# 1. Shipment
 ## 1.1 Shipment
  ### 1.1.1 ShipmentListView
  ### 1.1.2 ShipmentDetailView
  ### 1.1.3 CreateShipmentView
  ### 1.1.4 ShipmentUpdateView
  ### 1.1.5 ShipmentDeleteView
 ## 1.2 ShipmentProduct
  ### 1.2.1 ShipmentProductListView
  ### 1.2.2 CreateShipmentProductView
  ### 1.2.3 ShipmentProductUpdateView
  ### 1.2.4 ShipmentProductDeleteView

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
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Shipping'))
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

 ## 1.2 ShipmentProduct
  ### 1.2.1 ShipmentProductListView
class ShipmentProductListView(LoginRequiredMixin,ListView):
    model = ShipmentProduct
    template_name = 'shipmentproduct/shipmentproduct_list.html'

    def get_queryset(self):
        shipment_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=shipment_id)
        return ShipmentProduct.objects.filter(shipment_id = shipment_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"product"}
        context['shipment_id'] = self.kwargs['pk']
        context['shipment'] = self.shipment
        return context

  ### 1.2.2 CreateShipmentProductView
class CreateShipmentProductView(LoginRequiredMixin,CreateView):
    form_class = ShipmentProductForm
    model = ShipmentProduct
    template_name = 'shipmentproduct/shipmentproduct_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.shipment = Shipment.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"product"}
        shipment_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=shipment_id)
        context['shipment'] = self.shipment
        context['form'].fields['product'].queryset = OrderProduct.objects.filter(order_id=self.shipment.order_id)
        return context

  ### 1.2.3 ShipmentProductUpdateView
class ShipmentProductUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ShipmentProductForm
    model = ShipmentProduct
    template_name = 'shipmentproduct/shipmentproduct_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"product"}
        shipmentproduct_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=(ShipmentProduct.objects.get(pk=shipmentproduct_id).shipment_id))
        context['shipment'] = self.shipment
        context['form'].fields['product'].queryset = OrderProduct.objects.filter(order_id=self.shipment.order_id)
        return context

  ### 1.2.4 ShipmentProductDeleteView
class ShipmentProductDeleteView(LoginRequiredMixin,DeleteView):
    model = ShipmentProduct
    template_name = 'shipmentproduct/shipmentproduct_confirm_delete.html'

    def get_queryset(self):
        shipmentproduct_id = self.kwargs['pk']
        self.shipment = Shipment.objects.get(pk=(ShipmentProduct.objects.get(pk=shipmentproduct_id).shipment_id))
        return ShipmentProduct.objects.filter(pk=shipmentproduct_id)

    def get_success_url(self):
        return reverse_lazy('shipping:shipmentproduct_list', kwargs={'pk': ShipmentProduct.objects.get(id=self.kwargs['pk']).shipment_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"shipping","menu3":"shipment","menu4":"product"}
        context['shipment'] = self.shipment
        return context
