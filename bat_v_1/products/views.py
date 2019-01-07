from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.urls import reverse_lazy
from products.models import Product, PackageMeasurement
from products.forms import ProductForm, PackageMeasurementForm
# Create your views here.

class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    paginate_by = 3

    def get_queryset(self):
        self.order_by = self.request.GET.get('order_by', self.queryset)
        if self.order_by is None:
            self.order_by = "-create_date"
        return Product.objects.all().order_by(self.order_by)

    def get_paginate_by(self, queryset):
        self.paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_list'] = (1,2,3,50,100)
        context['order_by_list'] = [('create_date','Created Date: ASC'),('-create_date','Created Date: DESC')]
        context['active_menu'] = "basic"
        context['active_submenu'] = "products"
        context['order_by'] = self.order_by

        extra_url = ''
        if self.order_by is not None:
            extra_url += '&order_by='+self.order_by
        if self.paginate_by is not None:
            extra_url += '&paginate_by='+str(self.paginate_by)

        context['extra_url'] = extra_url
        return context

class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = "basic"
        context['active_submenu'] = "products"
        return context

class CreateProductView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'products/product_detail.html'
    form_class = ProductForm
    model = Product

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = "basic"
        context['active_submenu'] = "products"
        return context

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'products/product_detail.html'
    form_class = ProductForm
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = "basic"
        context['active_submenu'] = "products"
        return context

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')

class PackageMeasurementListView(LoginRequiredMixin,ListView):
    model = PackageMeasurement

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return PackageMeasurement.objects.filter(product_id = product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = "basic"
        context['active_submenu'] = "products"
        context['product_id'] = self.kwargs['pk']
        return context

class CreatePackageMeasurementView(LoginRequiredMixin,CreateView):
    form_class = PackageMeasurementForm
    model = PackageMeasurement

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = Product.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = "basic"
        context['active_submenu'] = "products"
        context['product_id'] = self.kwargs['pk']
        return context
