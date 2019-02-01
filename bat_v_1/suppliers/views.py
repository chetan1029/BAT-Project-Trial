from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse, reverse_lazy
from suppliers.models import (Supplier, PaymentTerms, Contact, Bank, Contract,
                              ProductPrice, Mold, MoldFile, Aql, AqlFile,
                              Order, OrderProduct, OrderFile, OrderPayment,
                              OrderDelivery)
from suppliers.forms import (SupplierForm, PaymentTermsForm, ContactForm, BankForm, ContractForm,
                             ProductPriceForm, MoldForm, MoldFileForm, AqlForm,
                             AqlFileForm, OrderForm, OrderProductForm, OrderFileForm,
                             OrderPaymentForm, OrderDeliveryForm, ContactFormSet)
from products.models import (Product)
from settings.models import (Status, Category)
from django.db.models import Q, ProtectedError
from django import forms
from django.db import IntegrityError, transaction
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
# 1. Payment Terms
 ## 1.1 PaymentTermsListView
 ## 1.2 CreatePaymentTermsView
 ## 1.3 PaymentTermsUpdateView
 ## 1.4 PaymentTermsDeleteView
# 2. Supplier
 ## 2.1 Supplier
  ### 2.1.1 SupplierListView
  ### 2.1.2 SupplierDetailView
  ### 2.1.3 CreateSupplierView
  ### 2.1.4 SupplierUpdateView
  ### 2.1.5 SupplierDeleteView
 ## 2.2 Contact
  ### 2.2.1 ContactListView
  ### 2.2.2 CreateContactView
  ### 2.2.3 ContactUpdateView
  ### 2.2.4 ContactDeleteView
 ## 2.3 Bank
  ### 2.3.1 BankListView
  ### 2.3.2 BankDetailView
  ### 2.3.3 CreateBankView
  ### 2.3.4 BankUpdateView
  ### 2.3.5 BankDeleteView
 ## 2.4 Contract
  ### 2.4.1 ContractListView
  ### 2.4.2 CreateContractView
  ### 2.4.3 ContractUpdateView
  ### 2.4.4 ContractDeleteView
 ## 2.5 ProductPrice
  ### 2.5.1 ProductPriceListView
  ### 2.5.2 CreateProductPriceView
  ### 2.5.3 ProductPriceUpdateView
  ### 2.5.4 ProductPriceDeleteView
 ## 2.6 Mold
  ### 2.6.1 Mold
   #### 2.6.1.1 MoldListView
   #### 2.6.1.2 MoldDetailView
   #### 2.6.1.3 CreateMoldView
   #### 2.6.1.4 MoldUpdateView
   #### 2.6.1.5 MoldDeleteView
  ### 2.6.2 MoldFile
   #### 2.6.2.1 MoldFileListView
   #### 2.6.2.2 CreateMoldFileView
   #### 2.6.2.3 MoldFileUpdateView
   #### 2.6.2.4 MoldFileDeleteView
 ## 2.7 Aql
  ### 2.7.1 Aql
   #### 2.7.1.1 AqlListView
   #### 2.7.1.2 AqlDetailView
   #### 2.7.1.3 CreateAqlView
   #### 2.7.1.4 AqlUpdateView
   #### 2.7.1.5 AqlDeleteView
  ### 2.7.2 AqlFile
   #### 2.7.2.1 AqlFileListView
   #### 2.7.2.2 CreateAqlFileView
   #### 2.7.2.3 AqlFileUpdateView
   #### 2.7.2.4 AqlFileDeleteView
 ## 2.8 Order
  ### 2.8.1 Order
   #### 2.8.1.1 OrderListView
   #### 2.8.1.2 CreateOrderView
   #### 2.8.1.3 OrderUpdateView
   #### 2.8.1.4 OrderDeleteView
  ### 2.8.2 OrderProduct
   #### 2.8.2.1 OrderProductListView
   #### 2.8.2.2 CreateOrderProductView
   #### 2.8.2.3 OrderProductUpdateView
   #### 2.8.2.4 OrderProductDeleteView
  ### 2.8.3 OrderFile
   #### 2.8.3.1 OrderFileListView
   #### 2.8.3.2 CreateOrderFileView
   #### 2.8.3.3 OrderFileUpdateView
   #### 2.8.3.4 OrderFileDeleteView
  ### 2.8.4 OrderPayment
   #### 2.8.4.1 OrderPaymentListView
   #### 2.8.4.2 CreateOrderPaymentView
   #### 2.8.4.3 OrderPaymentUpdateView
   #### 2.8.4.4 OrderPaymentDeleteView
  ### 2.8.5 OrderDelivery
   #### 2.8.5.1 OrderDeliveryListView
   #### 2.8.5.2 CreateOrderDeliveryView
   #### 2.8.5.3 OrderDeliveryUpdateView
   #### 2.8.5.4 OrderDeliveryDeleteView

# 1. Payment Terms
 ## 1.1 PaymentTermsListView
class PaymentTermsListView(LoginRequiredMixin,ListView):
    model = PaymentTerms
    template_name = 'paymentterms/paymentterms_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"paymentterms"}
        return context

 ## 1.2 CreatePaymentTermsView
class CreatePaymentTermsView(LoginRequiredMixin,CreateView):
    form_class = PaymentTermsForm
    model = PaymentTerms
    template_name = 'paymentterms/paymentterms_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.title = "PAY"+str(self.object.days)+"-"+str(self.object.prepay)
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"paymentterms"}
        return context

 ## 1.3 PaymentTermsUpdateView
class PaymentTermsUpdateView(LoginRequiredMixin,UpdateView):
    form_class = PaymentTermsForm
    model = PaymentTerms
    template_name = 'paymentterms/paymentterms_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.title = "PAY"+str(self.object.days)+"-"+str(self.object.prepay)
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"paymentterms"}
        return context

 ## 1.4 PaymentTermsDeleteView
class PaymentTermsDeleteView(LoginRequiredMixin,DeleteView):
    model = PaymentTerms
    template_name = 'paymentterms/paymentterms_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:paymentterms_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"paymentterms"}
        return context

# 2. Supplier
 ## 2.1 Supplier
  ### 2.1.1 SupplierListView
class SupplierListView(LoginRequiredMixin,ListView):
    model = Supplier
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
            queryset = Supplier.objects.all().order_by(self.order_by)
        elif self.search_q is not None and not self.category_q:
            queryset = Supplier.objects.filter(name__icontains=self.search_q)
        elif self.search_q is None and self.category_q:
            queryset = Supplier.objects.filter(category__id=self.category_q)
        else:
            queryset = Supplier.objects.filter(name__icontains=self.search_q, category__id=self.category_q)
        return queryset

    def get_paginate_by(self, queryset):
        self.paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_list'] = (2,10,20,50,100)
        context['order_by_list'] = [('create_date','Created Date: ASC'),('-create_date','Created Date: DESC')]
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        context['order_by'] = self.order_by
        context['item_view'] = self.item_view
        if self.search_q is None:
            context['search_q'] = ""
        else:
            context['search_q'] = self.search_q

        if not self.category_q:
            context['category_q'] = ""
            context['category_q_parent'] = Category.objects.get(name__exact='Suppliers').pk
        else:
            context['category_q'] = self.category_q
            context['category_q_parent'] = Category.objects.get(pk=self.category_q).parent_id

        extra_url = ''
        if self.order_by is not None:
            extra_url += '&order_by='+self.order_by
        if self.paginate_by is not None:
            extra_url += '&paginate_by='+str(self.paginate_by)
        if self.search_q is not None:
            extra_url += '&search_q='+self.search_q
        if self.category_q is not None:
            extra_url += '&category_q='+self.category_q

        context['extra_url'] = extra_url
        return context

  ### 2.1.2 SupplierDetailView
class SupplierDetailView(LoginRequiredMixin,DetailView):
    model = Supplier

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"details"}
        context['pk'] = self.kwargs['pk']
        return context

  ### 2.1.3 CreateSupplierView
class CreateSupplierView(LoginRequiredMixin,CreateView):
    form_class = SupplierForm
    model = Supplier

    def form_valid(self, form):
        # self.object = form.save(commit=False)
        # self.object.user = self.request.user
        # self.object.save()
        # return super().form_valid(form)
        context = self.get_context_data()
        contacts = context['contacts']
        with transaction.atomic():
            self.object = form.save()

            if contacts.is_valid():
                contacts.instance = self.object
                contacts.save()
        return super(CreateSupplierView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        # return context
        context = super(CreateSupplierView, self).get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        context['parent_category_id'] = Category.objects.get(name__exact="Suppliers").pk
        if self.request.POST:
            context['contacts'] = ContactFormSet(self.request.POST)
        else:
            context['contacts'] = ContactFormSet()
        return context

  ### 2.1.4 SupplierUpdateView
class SupplierUpdateView(LoginRequiredMixin,UpdateView):
    form_class = SupplierForm
    model = Supplier

    def form_valid(self, form):
        # self.object = form.save(commit=False)
        # self.object.update_date = timezone.now()
        # self.object.save()
        # return super().form_valid(form)
        context = self.get_context_data()
        contacts = context['contacts']
        with transaction.atomic():
            self.object = form.save()

            if contacts.is_valid():
                contacts.instance = self.object
                contacts.save()
        return super(SupplierUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        # return context
        context = super(SupplierUpdateView, self).get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        self.category = Category.objects.get(pk=self.get_object().category_id);
        context['category_name'] =  self.category.name
        context['parent_category_id'] = self.category.parent_id

        if self.request.POST:
            context['contacts'] = ContactFormSet(self.request.POST, instance=self.object)
        else:
            context['contacts'] = ContactFormSet(instance=self.object)
        return context

  ### 2.1.5 SupplierDeleteView
class SupplierDeleteView(LoginRequiredMixin,DeleteView):
    model = Supplier
    success_url = reverse_lazy('suppliers:supplier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        return context

  ### 2.1.6 View Functions for Supplier
def load_display_categories(request):
    category_id = request.GET.get('category')
    active = request.GET.get('active')
    if active:
        active = int(active)
    parent_category_id = Category.objects.get(pk=category_id).parent_id
    subcategory = Category.objects.filter(parent=category_id)
    return render(request, 'suppliers/ajax/category_display.html',{'categories':subcategory,'category_id':category_id,'parent_category_id':parent_category_id,'active':active})


 ## 2.2 Contact
  ### 2.2.1 ContactListView
class ContactListView(LoginRequiredMixin,ListView):
    model = Contact
    template_name = 'contact/contact_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        return Contact.objects.filter(supplier_id = supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contact"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        return context

  ### 2.2.2 CreateContactView
class CreateContactView(LoginRequiredMixin,CreateView):
    form_class = ContactForm
    model = Contact
    template_name = 'contact/contact_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.supplier = Supplier.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contact"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        return context

  ### 2.2.3 ContactUpdateView
class ContactUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ContactForm
    model = Contact
    template_name = 'contact/contact_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contact"}
        context['supplier'] = Supplier.objects.get(pk=Contact.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

  ### 2.2.4 ContactDeleteView
class ContactDeleteView(LoginRequiredMixin,DeleteView):
    model = Contact
    template_name = 'contact/contact_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:contact_list', kwargs={'pk': Contact.objects.get(id=self.kwargs['pk']).supplier_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contact"}
        context['supplier'] = Supplier.objects.get(pk=Contact.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

 ## 2.3 Bank
  ### 2.3.1 BankListView
class BankListView(LoginRequiredMixin,ListView):
    model = Bank
    template_name = 'bank/bank_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        return Bank.objects.filter(supplier_id = supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"bank"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        return context

  ### 2.3.2 BankDetailView
class BankDetailView(LoginRequiredMixin,DetailView):
    model = Bank
    template_name = 'bank/bank_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"bank"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        return context

  ### 2.3.3 CreateBankView
class CreateBankView(LoginRequiredMixin,CreateView):
    form_class = BankForm
    model = Bank
    template_name = 'bank/bank_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.supplier = Supplier.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"bank"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        return context

  ### 2.3.4 BankUpdateView
class BankUpdateView(LoginRequiredMixin,UpdateView):
    form_class = BankForm
    model = Bank
    template_name = 'bank/bank_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"bank"}
        context['supplier'] = Supplier.objects.get(pk=Bank.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

  ### 2.3.5 BankDeleteView
class BankDeleteView(LoginRequiredMixin,DeleteView):
    model = Bank
    template_name = 'bank/bank_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:bank_list', kwargs={'pk': Bank.objects.get(id=self.kwargs['pk']).supplier_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"bank"}
        context['supplier'] = Supplier.objects.get(pk=Bank.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

 ## 2.4 Contract
  ### 2.4.1 ContractListView
class ContractListView(LoginRequiredMixin,ListView):
    model = Contract
    template_name = 'contract/contract_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        return Contract.objects.filter(supplier_id = supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contract"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        return context

  ### 2.4.2 CreateContractView
class CreateContractView(LoginRequiredMixin,CreateView):
    form_class = ContractForm
    model = Contract
    template_name = 'contract/contract_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.supplier = Supplier.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contract"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        return context

  ### 2.4.3 ContractUpdateView
class ContractUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ContractForm
    model = Contract
    template_name = 'contract/contract_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contract"}
        context['supplier'] = Supplier.objects.get(pk=Contract.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

  ### 2.4.4 ContractDeleteView
class ContractDeleteView(LoginRequiredMixin,DeleteView):
    model = Contract
    template_name = 'contract/contract_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:contract_list', kwargs={'pk': Contract.objects.get(id=self.kwargs['pk']).supplier_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contract"}
        context['supplier'] = Supplier.objects.get(pk=Contract.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

 ## 2.5 ProductPrice
  ### 2.5.1 ProductPriceListView
class ProductPriceListView(LoginRequiredMixin,ListView):
    model = ProductPrice
    template_name = 'productprice/productprice_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        return ProductPrice.objects.filter(supplier_id = supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"product"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        return context

  ### 2.5.2 CreateProductPriceView
class CreateProductPriceView(LoginRequiredMixin,CreateView):
    form_class = ProductPriceForm
    model = ProductPrice
    template_name = 'productprice/productprice_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.supplier = Supplier.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"product"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        return context

  ### 2.5.3 ProductPriceUpdateView
class ProductPriceUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ProductPriceForm
    model = ProductPrice
    template_name = 'productprice/productprice_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"product"}
        context['supplier'] = Supplier.objects.get(pk=ProductPrice.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

  ### 2.5.4 ProductPriceDeleteView
class ProductPriceDeleteView(LoginRequiredMixin,DeleteView):
    model = ProductPrice
    template_name = 'productprice/productprice_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:productprice_list', kwargs={'pk': ProductPrice.objects.get(id=self.kwargs['pk']).supplier_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"product"}
        context['supplier'] = Supplier.objects.get(pk=ProductPrice.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

 ## 2.6 Mold
  ### 2.6.1 Mold
   #### 2.6.1.1 MoldListView
class MoldListView(LoginRequiredMixin,ListView):
    model = Mold
    template_name = 'mold/mold_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        return Mold.objects.filter(supplier_id = supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        return context

   #### 2.6.1.2 MoldDetailView
class MoldDetailView(LoginRequiredMixin,DetailView):
    model = Mold
    template_name = 'mold/mold_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"detail"}
        context['supplier'] = Supplier.objects.get(pk=Mold.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

   #### 2.6.1.3 CreateMoldView
class CreateMoldView(LoginRequiredMixin,CreateView):
    form_class = MoldForm
    model = Mold
    template_name = 'mold/mold_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.supplier = Supplier.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        return context

   #### 2.6.1.4 MoldUpdateView
class MoldUpdateView(LoginRequiredMixin,UpdateView):
    form_class = MoldForm
    model = Mold
    template_name = 'mold/mold_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold"}
        context['supplier'] = Supplier.objects.get(pk=Mold.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

   #### 2.6.1.5 MoldDeleteView
class MoldDeleteView(LoginRequiredMixin,DeleteView):
    model = Mold
    template_name = 'mold/mold_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:mold_list', kwargs={'pk': Mold.objects.get(id=self.kwargs['pk']).supplier_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold"}
        context['supplier'] = Supplier.objects.get(pk=Mold.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

  ### 2.6.2 MoldFile
   #### 2.6.2.1 MoldFileListView
class MoldFileListView(LoginRequiredMixin,ListView):
    model = MoldFile
    template_name = 'moldfile/moldfile_list.html'

    def get_queryset(self):
        mold_id = self.kwargs['pk']
        self.mold = Mold.objects.get(pk=mold_id)
        self.supplier = Supplier.objects.get(pk=self.mold.supplier_id)
        return MoldFile.objects.filter(mold_id = mold_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"file"}
        context['mold_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['mold'] = self.mold
        return context

   #### 2.6.2.2 CreateMoldFileView
 ### not using query_set here because it don't work with createview
class CreateMoldFileView(LoginRequiredMixin,CreateView):
    form_class = MoldFileForm
    model = MoldFile
    template_name = 'moldfile/moldfile_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.mold = Mold.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"file"}
        mold_id = self.kwargs['pk']
        self.mold = Mold.objects.get(pk=mold_id)
        self.supplier = Supplier.objects.get(pk=self.mold.supplier_id)
        context['supplier'] = self.supplier
        context['mold'] = self.mold
        return context

   #### 2.6.2.3 MoldFileUpdateView
class MoldFileUpdateView(LoginRequiredMixin,UpdateView):
    form_class = MoldFileForm
    model = MoldFile
    template_name = 'moldfile/moldfile_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"file"}
        moldfile_id = self.kwargs['pk']
        self.mold = Mold.objects.get(pk=MoldFile.objects.get(id=moldfile_id).mold_id)
        self.supplier = Supplier.objects.get(pk=self.mold.supplier_id)
        context['supplier'] = self.supplier
        context['mold'] = self.mold
        return context

   #### 2.6.2.4 MoldFileDeleteView
class MoldFileDeleteView(LoginRequiredMixin,DeleteView):
    model = MoldFile
    template_name = 'moldfile/moldfile_confirm_delete.html'

    def get_queryset(self):
        moldfile_id = self.kwargs['pk']
        self.mold = Mold.objects.get(pk=MoldFile.objects.get(id=moldfile_id).mold_id)
        self.supplier = Supplier.objects.get(pk=self.mold.supplier_id)
        return MoldFile.objects.filter(pk=moldfile_id)

    def get_success_url(self):
        return reverse_lazy('suppliers:moldfile_list', kwargs={'pk': MoldFile.objects.get(id=self.kwargs['pk']).mold_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"file"}
        context['supplier'] = self.supplier
        context['mold'] = self.mold
        return context

 ## 2.7 Aql
  ### 2.7.1 Aql
   #### 2.7.1.1 AqlListView
class AqlListView(LoginRequiredMixin,ListView):
    model = Aql
    template_name = 'aql/aql_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        return Aql.objects.filter(supplier_id=supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        return context

   #### 2.7.1.2 AqlDetailView
class AqlDetailView(LoginRequiredMixin,DetailView):
    model = Aql
    template_name = 'aql/aql_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql","menu5":"detail"}
        context['supplier'] = Supplier.objects.get(pk=Aql.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

   #### 2.7.1.3 CreateAqlView
class CreateAqlView(LoginRequiredMixin,CreateView):
    form_class = AqlForm
    model = Aql
    template_name = 'aql/aql_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.supplier = Supplier.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        # Commented for reference if we want to use similar code for diff form filters etc.
        #context['form'].fields['productprice'].queryset = ProductPrice.objects.filter(supplier_id=self.kwargs['pk'])
        return context

   #### 2.7.1.4 AqlUpdateView
class AqlUpdateView(LoginRequiredMixin,UpdateView):
    form_class = AqlForm
    model = Aql
    template_name = 'aql/aql_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql"}
        context['supplier'] = Supplier.objects.get(pk=Aql.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

   #### 2.7.1.5 AqlDeleteView
class AqlDeleteView(LoginRequiredMixin,DeleteView):
    model = Aql
    template_name = 'aql/aql_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:aql_list', kwargs={'pk': Aql.objects.get(id=self.kwargs['pk']).supplier_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql"}
        context['supplier'] = Supplier.objects.get(pk=Aql.objects.get(id=self.kwargs['pk']).supplier_id)
        return context

  ### 2.7.2 AqlFile
   #### 2.7.2.1 AqlFileListView
class AqlFileListView(LoginRequiredMixin,ListView):
    model = AqlFile
    template_name = 'aqlfile/aqlfile_list.html'

    def get_queryset(self):
        aql_id = self.kwargs['pk']
        self.aql = Aql.objects.get(pk=aql_id)
        self.supplier = Supplier.objects.get(pk=self.aql.supplier_id)
        return AqlFile.objects.filter(aql_id = aql_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql","menu5":"file"}
        context['aql_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['aql'] = self.aql
        return context

   #### 2.7.2.2 CreateAqlFileView
 ### not using query_set here because it don't work with createview
class CreateAqlFileView(LoginRequiredMixin,CreateView):
    form_class = AqlFileForm
    model = AqlFile
    template_name = 'aqlfile/aqlfile_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.aql = Aql.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql","menu5":"file"}
        aql_id = self.kwargs['pk']
        self.aql = Aql.objects.get(pk=aql_id)
        self.supplier = Supplier.objects.get(pk=self.aql.supplier_id)
        context['supplier'] = self.supplier
        context['aql'] = self.aql
        return context

   #### 2.7.2.3 AqlFileUpdateView
class AqlFileUpdateView(LoginRequiredMixin,UpdateView):
    form_class = AqlFileForm
    model = AqlFile
    template_name = 'aqlfile/aqlfile_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql","menu5":"file"}
        aqlfile_id = self.kwargs['pk']
        self.aql = Aql.objects.get(pk=AqlFile.objects.get(id=aqlfile_id).aql_id)
        self.supplier = Supplier.objects.get(pk=self.aql.supplier_id)
        context['supplier'] = self.supplier
        context['aql'] = self.aql
        return context

   #### 2.7.2.4 AqlFileDeleteView
class AqlFileDeleteView(LoginRequiredMixin,DeleteView):
    model = AqlFile
    template_name = 'aqlfile/aqlfile_confirm_delete.html'

    def get_queryset(self):
        aqlfile_id = self.kwargs['pk']
        self.aql = Aql.objects.get(pk=AqlFile.objects.get(id=aqlfile_id).aql_id)
        self.supplier = Supplier.objects.get(pk=self.aql.supplier_id)
        return AqlFile.objects.filter(pk=aqlfile_id)

    def get_success_url(self):
        return reverse_lazy('suppliers:aqlfile_list', kwargs={'pk': AqlFile.objects.get(id=self.kwargs['pk']).aql_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql","menu5":"file"}
        context['supplier'] = self.supplier
        context['aql'] = self.aql
        return context

 ## 2.8 Order
  ### 2.8.1 Order
   #### 2.8.1.1 OrderListView
class OrderListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'order/order_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        return Order.objects.filter(aql_id__in=Aql.objects.filter(supplier_id=supplier_id))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        return context

   #### 2.8.1.2 OrderDetailView
class OrderDetailView(LoginRequiredMixin,DetailView):
    model = Order
    template_name = 'order/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"detail"}
        context['supplier'] = Supplier.objects.get(pk=Aql.objects.get(pk=Order.objects.get(pk=self.kwargs['pk']).aql_id).supplier_id)
        return context

   #### 2.8.1.3 CreateOrderView
class CreateOrderView(LoginRequiredMixin,CreateView):
    form_class = OrderForm
    model = Order
    template_name = 'order/order_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.supplier = Supplier.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        context['form'].fields['aql'].queryset = Aql.objects.filter(supplier_id=self.kwargs['pk'])
        context['form'].fields['contact'].queryset = Contact.objects.filter(supplier_id=self.kwargs['pk'])
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Order'))
        return context

   #### 2.8.1.4 OrderUpdateView
class OrderUpdateView(LoginRequiredMixin,UpdateView):
    form_class = OrderForm
    model = Order
    template_name = 'order/order_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order"}
        context['supplier'] = Supplier.objects.get(pk=Aql.objects.get(pk=Order.objects.get(pk=self.kwargs['pk']).aql_id).supplier_id)
        context['form'].fields['aql'].queryset = Aql.objects.filter(supplier_id=self.kwargs['pk'])
        context['form'].fields['contact'].queryset = Contact.objects.filter(supplier_id=self.kwargs['pk'])
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Order'))
        return context

   #### 2.8.1.5 OrderDeleteView
class OrderDeleteView(LoginRequiredMixin,DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:order_list', kwargs={'pk': Aql.objects.get(pk=Order.objects.get(pk=self.kwargs['pk']).aql_id).supplier_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order"}
        context['supplier'] = Supplier.objects.get(pk=Aql.objects.get(pk=Order.objects.get(pk=self.kwargs['pk']).aql_id).supplier_id)
        return context

  ### 2.8.2 OrderProduct
   #### 2.8.2.1 OrderProductListView
class OrderProductListView(LoginRequiredMixin,ListView):
    model = OrderProduct
    template_name = 'orderproduct/orderproduct_list.html'

    def get_queryset(self):
        order_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        return OrderProduct.objects.filter(order_id = order_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"product"}
        context['aql_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

   #### 2.8.2.2 CreateOrderProductView
 ### not using query_set here because it don't work with createview
class CreateOrderProductView(LoginRequiredMixin,CreateView):
    form_class = OrderProductForm
    model = OrderProduct
    template_name = 'orderproduct/orderproduct_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.order = Order.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"product"}
        order_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        context['supplier'] = self.supplier
        context['order'] = self.order
        context['form'].fields['product'].queryset = Aql.objects.get(pk=self.order.aql_id).product.all()
        return context

   #### 2.8.2.3 OrderProductUpdateView
class OrderProductUpdateView(LoginRequiredMixin,UpdateView):
    form_class = OrderProductForm
    model = OrderProduct
    template_name = 'orderproduct/orderproduct_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"product"}
        orderproduct_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=OrderProduct.objects.get(id=orderproduct_id).order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        context['supplier'] = self.supplier
        context['order'] = self.order
        context['form'].fields['product'].queryset = AqlProduct.objects.filter(aql_id=self.order.aql_id).select_related()
        return context

   #### 2.8.2.4 OrderProductDeleteView
class OrderProductDeleteView(LoginRequiredMixin,DeleteView):
    model = OrderProduct
    template_name = 'orderproduct/orderproduct_confirm_delete.html'

    def get_queryset(self):
        orderproduct_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=OrderProduct.objects.get(id=orderproduct_id).order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        return OrderProduct.objects.filter(pk=orderproduct_id)

    def get_success_url(self):
        return reverse_lazy('suppliers:orderproduct_list', kwargs={'pk': OrderProduct.objects.get(id=self.kwargs['pk']).order_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"product"}
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

  ### 2.8.3 OrderFile
   #### 2.8.3.1 OrderFileListView
class OrderFileListView(LoginRequiredMixin,ListView):
    model = OrderFile
    template_name = 'orderfile/orderfile_list.html'

    def get_queryset(self):
        order_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        return OrderFile.objects.filter(order_id = order_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"file"}
        context['order_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

   #### 2.8.3.2 CreateOrderFileView
 ### not using query_set here because it don't work with createview
class CreateOrderFileView(LoginRequiredMixin,CreateView):
    form_class = OrderFileForm
    model = OrderFile
    template_name = 'orderfile/orderfile_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.order = Order.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"file"}
        order_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

   #### 2.8.3.3 OrderFileUpdateView
class OrderFileUpdateView(LoginRequiredMixin,UpdateView):
    form_class = OrderFileForm
    model = OrderFile
    template_name = 'orderfile/orderfile_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"file"}
        orderfile_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=OrderFile.objects.get(id=orderfile_id).order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

   #### 2.8.3.4 OrderFileDeleteView
class OrderFileDeleteView(LoginRequiredMixin,DeleteView):
    model = OrderFile
    template_name = 'orderfile/orderfile_confirm_delete.html'

    def get_queryset(self):
        orderfile_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=OrderFile.objects.get(id=orderfile_id).order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        return OrderFile.objects.filter(pk=orderfile_id)

    def get_success_url(self):
        return reverse_lazy('suppliers:orderfile_list', kwargs={'pk': OrderFile.objects.get(id=self.kwargs['pk']).order_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"file"}
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

  ### 2.8.4 OrderPayment
   #### 2.8.4.1 OrderPaymentListView
class OrderPaymentListView(LoginRequiredMixin,ListView):
    model = OrderPayment
    template_name = 'orderpayment/orderpayment_list.html'

    def get_queryset(self):
        order_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        return OrderPayment.objects.filter(order_id = order_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"payment"}
        context['aql_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

   #### 2.8.4.2 CreateOrderPaymentView
class CreateOrderPaymentView(LoginRequiredMixin,CreateView):
    form_class = OrderPaymentForm
    model = OrderPayment
    template_name = 'orderpayment/orderpayment_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.order = Order.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"payment"}
        order_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        context['supplier'] = self.supplier
        context['order'] = self.order
        context['form'].fields['bank'].queryset = Bank.objects.filter(supplier_id=self.supplier.id)
        return context

   #### 2.8.4.3 OrderPaymentUpdateView
class OrderPaymentUpdateView(LoginRequiredMixin,UpdateView):
    form_class = OrderPaymentForm
    model = OrderPayment
    template_name = 'orderpayment/orderpayment_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"payment"}
        orderpayment_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=OrderPayment.objects.get(id=orderpayment_id).order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        context['supplier'] = self.supplier
        context['order'] = self.order
        context['form'].fields['bank'].queryset = Bank.objects.filter(supplier_id=self.supplier.id)
        return context

   #### 2.8.4.4 OrderPaymentDeleteView
class OrderPaymentDeleteView(LoginRequiredMixin,DeleteView):
    model = OrderPayment
    template_name = 'orderpayment/orderpayment_confirm_delete.html'

    def get_queryset(self):
        orderpayment_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=OrderPayment.objects.get(id=orderpayment_id).order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        return OrderPayment.objects.filter(pk=orderpayment_id)

    def get_success_url(self):
        return reverse_lazy('suppliers:orderpayment_list', kwargs={'pk': OrderPayment.objects.get(id=self.kwargs['pk']).order_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"payment"}
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

  ### 2.8.5 OrderDelivery
   #### 2.8.5.1 OrderDeliveryListView
class OrderDeliveryListView(LoginRequiredMixin,ListView):
    model = OrderDelivery
    template_name = 'orderdelivery/orderdelivery_list.html'

    def get_queryset(self):
        order_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        return OrderDelivery.objects.filter(order_id = order_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"delivery"}
        context['aql_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

   #### 2.8.5.2 CreateOrderDeliveryView
class CreateOrderDeliveryView(LoginRequiredMixin,CreateView):
    form_class = OrderDeliveryForm
    model = OrderDelivery
    template_name = 'orderdelivery/orderdelivery_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.order = Order.objects.get(id=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"delivery"}
        order_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        context['supplier'] = self.supplier
        context['order'] = self.order
        context['form'].fields['status'].queryset = Status.objects.filter(parent_id=Status.objects.get(title__exact='Delivery'))
        return context

   #### 2.8.5.3 OrderDeliveryUpdateView
class OrderDeliveryUpdateView(LoginRequiredMixin,UpdateView):
    form_class = OrderDeliveryForm
    model = OrderDelivery
    template_name = 'orderdelivery/orderdelivery_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"delivery"}
        orderpayment_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=OrderDelivery.objects.get(id=orderpayment_id).order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context

   #### 2.8.5.4 OrderDeliveryDeleteView
class OrderDeliveryDeleteView(LoginRequiredMixin,DeleteView):
    model = OrderDelivery
    template_name = 'orderdelivery/orderdelivery_confirm_delete.html'

    def get_queryset(self):
        orderdelivery_id = self.kwargs['pk']
        self.order = Order.objects.get(pk=OrderDelivery.objects.get(id=orderdelivery_id).order_id)
        self.supplier = Supplier.objects.get(pk=(Aql.objects.get(pk=self.order.aql_id).supplier_id))
        return OrderDelivery.objects.filter(pk=orderdelivery_id)

    def get_success_url(self):
        return reverse_lazy('suppliers:orderdelivery_list', kwargs={'pk': OrderDelivery.objects.get(id=self.kwargs['pk']).order_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"delivery"}
        context['supplier'] = self.supplier
        context['order'] = self.order
        return context
