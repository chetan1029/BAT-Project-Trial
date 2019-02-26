from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from products.models import (Product, PackageMeasurement, ProductBundle, AmazonProduct, Box)
from settings.models import (Category, Status, Currency)
from products.forms import (ProductForm, PackageMeasurementForm, ProductBundleForm, AmazonProductForm, ProductBundleFormSet, BoxForm)
from django.db.models import Q
from django.utils.text import slugify
from django.db import IntegrityError, transaction
from django.http import JsonResponse
import logging
logger = logging.getLogger(__name__)
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
    paginate_by = 12

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
            queryset = Product.objects.exclude(ean="").order_by(self.order_by)
        elif self.search_q is not None and not self.category_q:
            queryset = Product.objects.filter(Q(title__icontains=self.search_q) | Q(sku__icontains=self.search_q)).exclude(ean="").order_by(self.order_by)
        elif self.search_q is None and self.category_q:
            queryset = Product.objects.filter(category__id=self.category_q).exclude(ean="")
        else:
            queryset = Product.objects.filter(Q(title__icontains=self.search_q) | Q(sku__icontains=self.search_q), category__id=self.category_q).exclude(ean="").order_by(self.order_by)
        return queryset

    def get_paginate_by(self, queryset):
        self.paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_list'] = (3,12,30,60,90)
        context['order_by_list'] = [('create_date','Created Date: ASC'),('-create_date','Created Date: DESC')]
        context['active_menu'] = {"menu1":"basic","menu2":"products"}
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
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"detail"}
        context['productbundles'] = ProductBundle.objects.filter(product_id=self.kwargs['pk'])
        logger.warning(context)
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
        context['active_menu'] = {"menu1":"basic","menu2":"products"}
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Products'))
        context['colors'] = Color.objects.all()
        context['sizes'] = Size.objects.all()
        return context

def create_product(request):
    form = ProductForm
    parent_category_id = Category.objects.get(name__exact="Products").pk
    active_menu = {"menu1":"basic","menu2":"products"}

    if request.method == 'POST':
        category = request.POST['category']
        category_i = Category.objects.get(pk=category)
        title = request.POST['title']
        status  = request.POST['status']
        status_i  = Status.objects.get(pk=status)
        variation  = request.POST['variation']

        if variation == "size":
            for size in request.POST.getlist('sizes[]'):
                if size:
                    size_url = slugify(size)
                    ean = request.POST.get('ean'+size_url,False)
                    if ean:
                        manufacturer_part_number = request.POST['manufacturer_part_number'+size_url]
                        sku = request.POST['sku'+size_url]
                        new_title = title+" "+size
                        color = ""
                        product = Product(title=new_title,category=category_i,ean=ean,manufacturer_part_number=manufacturer_part_number,sku=sku,status=status_i,size=size,color=color)
                        product.save()
        elif variation == "color":
            for color in request.POST.getlist('colors[]'):
                if color:
                    color_url = slugify(color)
                    ean = request.POST.get('ean'+color_url,False)
                    if ean:
                        manufacturer_part_number = request.POST['manufacturer_part_number'+color_url]
                        sku = request.POST['sku'+color_url]
                        new_title = title+" "+color
                        size = ""
                        product = Product(title=new_title,category=category_i,ean=ean,manufacturer_part_number=manufacturer_part_number,sku=sku,status=status_i,size=size,color=color)
                        product.save()
        elif variation == "color-size":
            for color in request.POST.getlist('colors[]'):
                for size in request.POST.getlist('sizes[]'):
                    if color and size:
                        color_url = slugify(color)
                        size_url = slugify(size)
                        ean = request.POST.get('ean'+color_url+''+size_url,False)
                        logger.warning('ean'+color_url+''+size_url)
                        if ean:
                            manufacturer_part_number = request.POST['manufacturer_part_number'+color_url+''+size_url]
                            sku = request.POST['sku'+color_url+''+size_url]
                            new_title = title+" "+size+" "+color
                            product = Product(title=new_title,category=category_i,ean=ean,manufacturer_part_number=manufacturer_part_number,sku=sku,status=status_i,size=size,color=color)
                            product.save()



        return redirect('products:product_list')
    return render(request,'products/product_form.html',{'form':form, 'active_menu':active_menu, 'parent_category_id':parent_category_id})

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
        context['active_menu'] = {"menu1":"basic","menu2":"products"}
        self.category = Category.objects.get(pk=self.get_object().category_id);
        context['category_name'] =  self.category.name
        context['parent_category_id'] = self.category.parent_id
        return context

  ### 1.1.5 ProductDeleteView
class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products"}
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

def generate_variation(request):
    get_colors = request.GET.get('colors')
    get_sizes = request.GET.get('sizes')
    if get_colors:
        colors = get_colors.split(',')
    else:
        colors = []

    if get_sizes:
        sizes = get_sizes.split(',')
    else:
        sizes = []
    return render(request, 'products/ajax/variation.html',{'sizes':sizes,'colors':colors})

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
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"packagemeasurement"}
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
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"packagemeasurement"}
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
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"packagemeasurement"}
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
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"packagemeasurement"}
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
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"productbundle"}
        context['product_id'] = self.kwargs['pk']
        context['product'] = self.product
        return context

  ### 1.3.2 CreateProductBundleView
class CreateProductBundleView(LoginRequiredMixin,CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'productbundle/productbundle_form.html'

    def form_valid(self, form):
        context = self.get_context_data()
        productbundles = context['productbundles']
        with transaction.atomic():
            self.object = form.save()

            if productbundles.is_valid():
                productbundles.instance = self.object
                productbundles.save()
        return super(CreateProductBundleView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateProductBundleView, self).get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"productbundle"}
        context['parent_category_id'] = Category.objects.get(name__exact="Products").pk
        if self.request.POST:
            context['productbundles'] = ProductBundleFormSet(self.request.POST)
        else:
            context['productbundles'] = ProductBundleFormSet()
        return context

  ### 1.3.3 ProductBundleUpdateView
class ProductBundleUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'productbundle/productbundle_form.html'

    def form_valid(self, form):
        context = self.get_context_data()
        productbundles = context['productbundles']
        logger.warning(productbundles)
        with transaction.atomic():
            self.object = form.save()

            if productbundles.is_valid():
                productbundles.instance = self.object
                productbundles.save()
        return super(ProductBundleUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductBundleUpdateView, self).get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"productbundle"}
        self.category = Category.objects.get(pk=self.get_object().category_id);
        context['category_name'] =  self.category.name
        context['parent_category_id'] = self.category.parent_id
        if self.request.POST:
            context['productbundles'] = ProductBundleFormSet(self.request.POST, instance=self.object)
        else:
            context['productbundles'] = ProductBundleFormSet(instance=self.object)
        return context

  ### 1.3.4 ProductBundleDeleteView
class ProductBundleDeleteView(LoginRequiredMixin,DeleteView):
    model = ProductBundle
    template_name = 'productbundle/productbundle_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('products:productbundle_list', kwargs={'pk': ProductBundle.objects.get(id=self.kwargs['pk']).product_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"productbundle"}
        context['product'] = Product.objects.get(pk=ProductBundle.objects.get(id=self.kwargs['pk']).product_id)
        return context

## 1.4 Box
 ### 1.4.1 BoxListView
class BoxListView(LoginRequiredMixin,ListView):
   model = Box
   template_name = 'box/box_list.html'
   def get_queryset(self):
       product_id = self.kwargs['pk']
       self.box_active = Box.objects.filter(product_id=product_id, type="Active")
       self.box_archived = Box.objects.filter(product_id=product_id, type="Archived")
       self.product = Product.objects.get(pk=product_id)
       return Box.objects.filter(product_id=product_id)

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"box"}
       context['product_id'] = self.kwargs['pk']
       context['product'] = self.product
       context['box_active'] = self.box_active
       context['box_archived'] = self.box_archived
       return context

 ### 1.4.2 CreateBoxView
class CreateBoxView(LoginRequiredMixin,CreateView):
   form_class = BoxForm
   model = Box
   template_name = 'box/box_form.html'

   def form_valid(self, form):
       self.object = form.save(commit=False)
       Box.objects.filter(product_id=self.kwargs['pk']).update(type="Archived")
       self.object.product = Product.objects.get(id=self.kwargs['pk'])
       self.object.title = str(self.object.length)+"x"+str(self.object.width)+"x"+str(self.object.depth);
       self.object.cbm = round(((self.object.length/100)*(self.object.width/100)*(self.object.depth/100)),3)
       self.object.type = "Active"
       self.object.save()
       return super().form_valid(form)

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"box"}
       context['product'] = Product.objects.get(pk=self.kwargs['pk'])
       return context

 ### 1.4.3 BoxUpdateView
class BoxUpdateView(LoginRequiredMixin,UpdateView):
   form_class = BoxForm
   model = Box
   template_name = 'box/box_form.html'

   def form_valid(self, form):
       self.object = form.save(commit=False)
       self.object.update_date = timezone.now()
       self.object.title = str(self.object.length)+"x"+str(self.object.width)+"x"+str(self.object.depth);
       self.object.cbm = round(((self.object.length/100)*(self.object.width/100)*(self.object.depth/100)),3)
       self.object.save()
       return super().form_valid(form)

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"box"}
       context['product'] = Product.objects.get(pk=Box.objects.get(id=self.kwargs['pk']).product_id)
       return context

 ### 1.4.4 BoxDeleteView
class BoxDeleteView(LoginRequiredMixin,DeleteView):
   model = Box
   template_name = 'box/box_confirm_delete.html'

   def get_success_url(self):
       return reverse_lazy('products:box_list', kwargs={'pk': Box.objects.get(id=self.kwargs['pk']).product_id})

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['active_menu'] = {"menu1":"basic","menu2":"products","menu3":"box"}
       context['product'] = Product.objects.get(pk=Box.objects.get(id=self.kwargs['pk']).product_id)
       return context

    #### 2.7.1.6 Function for Box
def change_box_type(request):
    box_id = request.GET.get('box_id')
    type = request.GET.get('type')
    box = Box.objects.get(pk=box_id)

    if type == "Active":
        Box.objects.filter(product=box.product).update(type="Archived")
    Box.objects.filter(pk=box_id).update(type=type)
    data = {
        'success': True
    }
    return JsonResponse(data)

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
