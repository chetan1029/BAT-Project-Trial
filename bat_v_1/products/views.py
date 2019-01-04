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

    def get_queryset(self):
        return Product.objects.all().order_by('-create_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = "basic"
        context['active_submenu'] = "products"
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
        return PackageMeasurement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = "basic"
        context['active_submenu'] = "products"
        return context

class CreatePackageMeasurementView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'products/packagemeasurement_list.html'
    form_class = PackageMeasurementForm
    model = PackageMeasurement

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
