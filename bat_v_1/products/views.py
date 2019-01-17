from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from products.models import (Product, PackageMeasurement, ProductBundle, Category, Status,
                             Currency, Color, Size)
from suppliers.models import Status
from products.forms import (ProductForm, PackageMeasurementForm, ProductBundleForm, CategoryForm, StatusForm,
                             CurrencyForm, ColorForm, SizeForm)
from django.db.models import Q
# Create your views here.
# 1. Category
 ## 1.1 CategoryListView
 ## 1.2 CreateCategoryView
 ## 1.3 CategoryUpdateView
 ## 1.4 CategoryDeleteView
# 2. Color
 ## 2.1 ColorListView
 ## 2.2 CreateColorView
 ## 2.3 ColorUpdateView
 ## 2.4 ColorDeleteView
# 3. Size
 ## 3.1 SizeListView
 ## 3.2 CreateSizeView
 ## 3.3 SizeUpdateView
 ## 3.4 SizeDeleteView
# 4. Status
 ## 4.1 StatusListView
 ## 4.2 CreateStatusView
 ## 4.3 StatusUpdateView
 ## 4.4 StatusDeleteView
# 5. Currecy
 ## 5.1 CurrecyListView
 ## 5.2 CreateCurrecyView
 ## 5.3 CurrecyUpdateView
 ## 5.4 CurrecyDeleteView
# 6. Product
 ## 6.1 Product
  ### 6.1.1 ProductListView
  ### 6.1.2 ProductDetailView
  ### 6.1.3 CreateProductView
  ### 6.1.4 ProductUpdateView
  ### 6.1.5 ProductDeleteView
 ## 6.2 PackageMeasurement
  ### 6.2.1 PackageMeasurementListView
  ### 6.2.2 CreatePackageMeasurementView
  ### 6.2.3 PackageMeasurementUpdateView
  ### 6.2.4 PackageMeasurementDeleteView
 ## 6.3 ProductBundle
  ### 6.3.1 ProductBundleListView
  ### 6.3.2 CreateProductBundleView
  ### 6.3.3 ProductBundleUpdateView
  ### 6.3.4 ProductBundleDeleteView

# 1. Category
 ## 1.1 CategoryListView
class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'category/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"category"}
        return context

 ## 1.2 CreateCategoryView
class CreateCategoryView(LoginRequiredMixin,CreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'category/category_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"category"}
        return context

 ## 1.3 CategoryUpdateView
class CategoryUpdateView(LoginRequiredMixin,UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'category/category_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"category"}
        return context

 ## 1.4 CategoryDeleteView
class CategoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('products:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"category"}
        return context

# 2. Color
 ## 2.1 ColorListView
class ColorListView(LoginRequiredMixin,ListView):
    model = Color
    template_name = 'color/color_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"color"}
        return context

 ## 2.2 CreateColorView
class CreateColorView(LoginRequiredMixin,CreateView):
    form_class = ColorForm
    model = Color
    template_name = 'color/color_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"color"}
        return context

 ## 2.3 ColorUpdateView
class ColorUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ColorForm
    model = Color
    template_name = 'color/color_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"color"}
        return context

 ## 2.4 ColorDeleteView
class ColorDeleteView(LoginRequiredMixin,DeleteView):
    model = Color
    template_name = 'color/color_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('products:color_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"color"}
        return context

# 3. Size
 ## 3.1 SizeListView
class SizeListView(LoginRequiredMixin,ListView):
    model = Size
    template_name = 'size/size_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"size"}
        return context

 ## 3.2 CreateSizeView
class CreateSizeView(LoginRequiredMixin,CreateView):
    form_class = SizeForm
    model = Size
    template_name = 'size/size_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"size"}
        return context

 ## 4.3 SizeUpdateView
class SizeUpdateView(LoginRequiredMixin,UpdateView):
    form_class = SizeForm
    model = Size
    template_name = 'size/size_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"size"}
        return context

 ## 4.4 SizeDeleteView
class SizeDeleteView(LoginRequiredMixin,DeleteView):
    model = Size
    template_name = 'size/size_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('products:size_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"size"}
        return context

# 4. Status
 ## 4.1 StatusListView
class StatusListView(LoginRequiredMixin,ListView):
    model = Status
    template_name = 'status/status_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"status"}
        return context

 ## 4.2 CreateStatusView
class CreateStatusView(LoginRequiredMixin,CreateView):
    form_class = StatusForm
    model = Status
    template_name = 'status/status_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"status"}
        return context

 ## 4.3 StatusUpdateView
class StatusUpdateView(LoginRequiredMixin,UpdateView):
    form_class = StatusForm
    model = Status
    template_name = 'status/status_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"status"}
        return context

 ## 4.4 StatusDeleteView
class StatusDeleteView(LoginRequiredMixin,DeleteView):
    model = Status
    template_name = 'status/status_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('products:status_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"status"}
        return context

# 5. Currency
 ## 5.1 CurrencyListView
class CurrencyListView(LoginRequiredMixin,ListView):
    model = Currency
    template_name = 'currency/currency_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"currency"}
        return context

 ## 5.2 CreateCurrencyView
class CreateCurrencyView(LoginRequiredMixin,CreateView):
    form_class = CurrencyForm
    model = Currency
    template_name = 'currency/currency_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"currency"}
        return context

 ## 5.3 CurrencyUpdateView
class CurrencyUpdateView(LoginRequiredMixin,UpdateView):
    form_class = CurrencyForm
    model = Currency
    template_name = 'currency/currency_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"currency"}
        return context

 ## 5.4 CurrencyDeleteView
class CurrencyDeleteView(LoginRequiredMixin,DeleteView):
    model = Currency
    template_name = 'currency/currency_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('products:currency_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"currency"}
        return context

# 6. Product
 ## 6.1 Product
  ### 6.1.1 ProductListView
class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    paginate_by = 10

    def get_queryset(self):
        self.order_by = self.request.GET.get('order_by', self.queryset)
        if self.order_by is None:
            self.order_by = "-create_date"

        self.search_q = self.request.GET.get('search_q', self.queryset)
        if self.search_q is None:
            queryset = Product.objects.all().order_by(self.order_by)
        else:
            queryset = Product.objects.filter(Q(title__icontains=self.search_q) | Q(sku__icontains=self.search_q)).order_by(self.order_by)
        return queryset

    def get_paginate_by(self, queryset):
        self.paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_list'] = (2,10,20,50,100)
        context['order_by_list'] = [('create_date','Created Date: ASC'),('-create_date','Created Date: DESC')]
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products"}
        context['order_by'] = self.order_by
        if self.search_q is None:
            context['search_q'] = ""
        else:
            context['search_q'] = self.search_q

        extra_url = ''
        if self.order_by is not None:
            extra_url += '&order_by='+self.order_by
        if self.paginate_by is not None:
            extra_url += '&paginate_by='+str(self.paginate_by)
        if self.search_q is not None:
            extra_url += '&search_q='+self.search_q

        context['extra_url'] = extra_url
        return context

  ### 6.1.2 ProductDetailView
class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"detail"}
        return context

  ### 6.1.3 CreateProductView
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
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products"}
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Product'))
        return context

  ### 6.1.4 ProductUpdateView
class ProductUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'products/product_detail.html'
    form_class = ProductForm
    model = Product

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products"}
        return context

  ### 6.1.5 ProductDeleteView
class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products"}
        return context

 ## 6.2 PackageMeasurement
  ### 6.2.1 PackageMeasurementListView
class PackageMeasurementListView(LoginRequiredMixin,ListView):
    model = PackageMeasurement
    template_name = 'packagemeasurement/packagemeasurement_list.html'

    def get_queryset(self):
        product_id = self.kwargs['pk']
        self.product = Product.objects.get(pk=product_id)
        return PackageMeasurement.objects.filter(product_id = product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"packagemeasurement"}
        context['product_id'] = self.kwargs['pk']
        context['product'] = self.product
        return context

  ### 6.2.2 CreatePackageMeasurementView
class CreatePackageMeasurementView(LoginRequiredMixin,CreateView):
    form_class = PackageMeasurementForm
    model = PackageMeasurement
    template_name = 'packagemeasurement/packagemeasurement_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = Product.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"packagemeasurement"}
        context['product'] = Product.objects.get(pk=self.kwargs['pk'])
        return context

  ### 6.2.3 PackageMeasurementUpdateView
class PackageMeasurementUpdateView(LoginRequiredMixin,UpdateView):
    form_class = PackageMeasurementForm
    model = PackageMeasurement
    template_name = 'packagemeasurement/packagemeasurement_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"packagemeasurement"}
        context['product'] = Product.objects.get(pk=PackageMeasurement.objects.get(id=self.kwargs['pk']).product_id)
        return context

  ### 6.2.4 PackageMeasurementDeleteView
class PackageMeasurementDeleteView(LoginRequiredMixin,DeleteView):
    model = PackageMeasurement
    template_name = 'packagemeasurement/packagemeasurement_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('products:packagemeasurement_list', kwargs={'pk': PackageMeasurement.objects.get(id=self.kwargs['pk']).product_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"packagemeasurement"}
        context['product'] = Product.objects.get(pk=PackageMeasurement.objects.get(id=self.kwargs['pk']).product_id)
        return context

 ## 6.3 ProductBundle
  ### 6.3.1 ProductBundleListView
class ProductBundleListView(LoginRequiredMixin,ListView):
    model = ProductBundle
    template_name = 'productbundle/productbundle_list.html'

    def get_queryset(self):
        product_id = self.kwargs['pk']
        self.product = Product.objects.get(pk=product_id)
        return ProductBundle.objects.filter(product_id = product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"productbundle"}
        context['product_id'] = self.kwargs['pk']
        context['product'] = self.product
        return context

  ### 6.3.2 CreateProductBundleView
class CreateProductBundleView(LoginRequiredMixin,CreateView):
    form_class = ProductBundleForm
    model = ProductBundle
    template_name = 'productbundle/productbundle_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = Product.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"productbundle"}
        context['product'] = Product.objects.get(pk=self.kwargs['pk'])
        return context

  ### 6.3.3 ProductBundleUpdateView
class ProductBundleUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ProductBundleForm
    model = ProductBundle
    template_name = 'productbundle/productbundle_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"productbundle"}
        context['product'] = Product.objects.get(pk=ProductBundle.objects.get(id=self.kwargs['pk']).product_id)
        return context

  ### 6.3.4 ProductBundleDeleteView
class ProductBundleDeleteView(LoginRequiredMixin,DeleteView):
    model = ProductBundle
    template_name = 'productbundle/productbundle_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('products:productbundle_list', kwargs={'pk': ProductBundle.objects.get(id=self.kwargs['pk']).product_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"productbundle"}
        context['product'] = Product.objects.get(pk=ProductBundle.objects.get(id=self.kwargs['pk']).product_id)
        return context
