from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from products.models import (Product, PackageMeasurement, ProductBundle, AmazonProduct)
from settings.models import (Category, Status, Currency, Color, Size)
from products.forms import (ProductForm, PackageMeasurementForm, ProductBundleForm, AmazonProductForm)
from django.db.models import Q
# Create your views here.
# 1. Product
 ## 1.1 Product
  ### 1.1.1 ProductListView
  ### 1.1.2 ProductDetailView
  ### 1.1.3 CreateProductView
  ### 1.1.4 ProductUpdateView
  ### 1.1.5 ProductDeleteView
 ## 1.2 PackageMeasurement
  ### 1.2.1 PackageMeasurementListView
  ### 1.2.2 CreatePackageMeasurementView
  ### 1.2.3 PackageMeasurementUpdateView
  ### 1.2.4 PackageMeasurementDeleteView
 ## 1.3 ProductBundle
  ### 1.3.1 ProductBundleListView
  ### 1.3.2 CreateProductBundleView
  ### 1.3.3 ProductBundleUpdateView
  ### 1.3.4 ProductBundleDeleteView
# 2. AmazonProduct
 ## 2.1 AmazonProduct
  ### 2.1.1 AmazonProductListView
  ### 2.1.2 AmazonProductDetailView
  ### 2.1.3 CreateAmazonProductView
  ### 2.1.4 AmazonProductUpdateView
  ### 2.1.5 AmazonProductDeleteView

# 1. Product
 ## 1.1 Product
  ### 1.1.1 ProductListView
class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    paginate_by = 10

    def get_queryset(self):
        self.order_by = self.request.GET.get('order_by', self.queryset)
        if self.order_by is None:
            self.order_by = "-create_date"

        self.item_view = self.request.GET.get('item_view', self.queryset)
        if self.item_view is None:
            self.item_view = "thumb_view"

        self.search_q = self.request.GET.get('search_q', self.queryset)
        self.category_q = self.request.GET.get('category_q', self.queryset)

        if self.search_q is None and not self.category_q:
            queryset = Product.objects.all().order_by(self.order_by)
        elif self.search_q is not None and not self.category_q:
            queryset = Product.objects.filter(Q(title__icontains=self.search_q) | Q(sku__icontains=self.search_q)).order_by(self.order_by)
        elif self.search_q is None and self.category_q:
            queryset = Product.objects.filter(category__id=self.category_q)
        else:
            queryset = Product.objects.filter(Q(title__icontains=self.search_q) | Q(sku__icontains=self.search_q), category__id=self.category_q).order_by(self.order_by)

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
        context['item_view'] = self.item_view
        if self.search_q is None:
            context['search_q'] = ""
        else:
            context['search_q'] = self.search_q

        if not self.category_q:
            context['category_q'] = ""
            context['category_q_parent'] = Category.objects.get(name__exact='Products').pk
        else:
            context['category_q'] = self.category_q
            context['category_q_parent'] = Category.objects.get(pk=self.category_q).parent_id

        extra_url = ''
        if self.order_by is not None:
            extra_url += '&order_by='+self.order_by
        if self.item_view is not None:
            extra_url += '&item_view='+self.item_view
        if self.paginate_by is not None:
            extra_url += '&paginate_by='+str(self.paginate_by)
        if self.search_q is not None:
            extra_url += '&search_q='+self.search_q
        if self.category_q is not None:
            extra_url += '&category_q='+self.category_q

        context['extra_url'] = extra_url
        return context

  ### 1.1.2 ProductDetailView
class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products","menu4":"detail"}
        return context

  ### 1.1.3 CreateProductView
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
        context['form'].fields['category'].queryset = Category.objects.filter(parent_id=Category.objects.get(name__exact='Products'))
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Products'))
        return context

  ### 1.1.4 ProductUpdateView
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
        context['form'].fields['category'].queryset = Category.objects.filter(parent_id=Category.objects.get(name__exact='Products'))
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Products'))
        return context

  ### 1.1.5 ProductDeleteView
class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"products"}
        return context

  ### 1.1.6 Views for Product
def load_categories(request):
    category_id = request.GET.get('category')
    subcategory = Category.objects.filter(parent=category_id)
    return render(request, 'products/ajax/category_list_drodown.html',{'categories':subcategory,'category_id':category_id})

def load_display_categories(request):
    category_id = request.GET.get('category')
    active = request.GET.get('active')
    if active:
        active = int(active)
    parent_category_id = Category.objects.get(pk=category_id).parent_id
    subcategory = Category.objects.filter(parent=category_id)
    return render(request, 'products/ajax/category_display.html',{'categories':subcategory,'category_id':category_id,'parent_category_id':parent_category_id,'active':active})


 ## 1.2 PackageMeasurement
  ### 1.2.1 PackageMeasurementListView
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

  ### 1.2.2 CreatePackageMeasurementView
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

  ### 1.2.3 PackageMeasurementUpdateView
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

  ### 1.2.4 PackageMeasurementDeleteView
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

 ## 1.3 ProductBundle
  ### 1.3.1 ProductBundleListView
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

  ### 1.3.2 CreateProductBundleView
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

  ### 1.3.3 ProductBundleUpdateView
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

  ### 1.3.4 ProductBundleDeleteView
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

# 2. AmazonProduct
 ## 2.1 AmazonProduct
  ### 2.1.1 AmazonProductListView
class AmazonProductListView(LoginRequiredMixin,ListView):
    model = AmazonProduct
    template_name = 'amazonproduct/amazonproduct_list.html'
    paginate_by = 10

    def get_queryset(self):
        self.order_by = self.request.GET.get('order_by', self.queryset)
        if self.order_by is None:
            self.order_by = "-create_date"

        self.search_q = self.request.GET.get('search_q', self.queryset)
        if self.search_q is None:
            queryset = AmazonProduct.objects.all().order_by(self.order_by)
        else:
            queryset = AmazonProduct.objects.filter(Q(title__icontains=self.search_q) | Q(sku__icontains=self.search_q)).order_by(self.order_by)
        return queryset

    def get_paginate_by(self, queryset):
        self.paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_list'] = (2,10,20,50,100)
        context['order_by_list'] = [('create_date','Created Date: ASC'),('-create_date','Created Date: DESC')]
        context['active_menu'] = {"menu1":"inventorize","menu2":"amazon-products"}
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

  ### 2.1.2 AmazonProductDetailView
class AmazonProductDetailView(LoginRequiredMixin,DetailView):
    model = AmazonProduct
    template_name = 'amazonproduct/amazonproduct_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"inventorize","menu2":"amazon-products","menu3":"detail"}
        return context

  ### 2.1.3 CreateAmazonProductView
class CreateAmazonProductView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'amazonproduct/amazonproduct_detail.html'
    form_class = AmazonProductForm
    model = AmazonProduct
    template_name = 'amazonproduct/amazonproduct_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"inventorize","menu2":"amazon-products"}
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Products'))
        return context

  ### 2.1.4 AmazonProductUpdateView
class AmazonProductUpdateView(LoginRequiredMixin,UpdateView):
    form_class = AmazonProductForm
    model = AmazonProduct
    template_name = 'amazonproduct/amazonproduct_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"inventorize","menu2":"amazon-products"}
        return context

  ### 2.1.5 AmazonProductDeleteView
class AmazonProductDeleteView(LoginRequiredMixin,DeleteView):
    model = AmazonProduct
    template_name = 'amazonproduct/amazonproduct_confirm_delete.html'
    success_url = reverse_lazy('products:amazonproduct_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"inventorize","menu2":"amazon-products"}
        return context
