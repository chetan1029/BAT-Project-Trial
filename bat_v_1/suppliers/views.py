from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse, reverse_lazy
from suppliers.models import (Supplier, PaymentTerms, Contact, Bank, Contract,
                              ProductPrice, Mold, MoldFile, MoldHost, Aql,
                              Order, OrderProduct, OrderFile, OrderPayment,
                              OrderDelivery, OrderDeliveryProduct, Certification, OrderDeliveryTestReport)
from suppliers.forms import (SupplierForm, PaymentTermsForm, ContactForm, BankForm, ContractForm,
                             ProductPriceForm, MoldForm, MoldFileForm, MoldHostForm, AqlForm,
                             OrderForm, OrderProductForm, OrderFileForm,
                             OrderPaymentForm, OrderDeliveryForm, OrderDeliveryProductForm, CertificationForm)
from products.models import (Product, ProductBundle)
from settings.models import (Status, Category, Currency, CompanySetting)
from django.db.models import Q, ProtectedError
from django import forms
from django.db import IntegrityError, transaction
from django.http import JsonResponse
from django.contrib import messages
from django.core import serializers
from django.db.models import Sum
from decimal import Decimal
from datetime import datetime, timedelta
from weasyprint import HTML, CSS
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.text import slugify
import logging
import os
logger = logging.getLogger(__name__)

VENDOR = "Vendors"
CAT_PRODUCT = "Products"
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
  ### 2.6.3 MoldFile
   #### 2.6.3.1 MoldHostListView
   #### 2.6.3.2 CreateMoldHostView
   #### 2.6.3.3 MoldHostUpdateView
   #### 2.6.3.4 MoldHostDeleteView
 ## 2.7 Aql
  ### 2.7.1 Aql
   #### 2.7.1.1 AqlListView
   #### 2.7.1.2 AqlDetailView
   #### 2.7.1.3 CreateAqlView
   #### 2.7.1.4 AqlUpdateView
   #### 2.7.1.5 AqlDeleteView
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
# 3 Certification
 ## 3.1 Certification
  ### 3.1.1 CertificationListView
  ### 3.1.2 CreateCertificationView
  ### 3.1.3 CertificationUpdateView
  ### 3.1.4 CertificationDeleteView

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
        deposit = self.object.deposit
        on_delivery = self.object.on_delivery
        remaining_per = int(100)-(int(deposit)+int(on_delivery))
        self.object.title = "PAY"+str(self.object.deposit)+"-"+str(self.object.on_delivery)+"-"+str(remaining_per)+"-"+str(self.object.payment_term)+"Days"
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
        remaining_per = int(100)-(int(self.object.deposit)+int(self.object.on_delivery))
        self.object.title = "PAY"+str(self.object.deposit)+"-"+str(self.object.on_delivery)+"-"+str(remaining_per)+"-"+str(self.object.payment_term)+"Days"
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
            context['category_q_parent'] = Category.objects.get(name__exact=VENDOR).pk
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        context['parent_category_id'] = Category.objects.get(name__exact=VENDOR).pk
        return context

  ### 2.1.4 SupplierUpdateView
class SupplierUpdateView(LoginRequiredMixin,UpdateView):
    form_class = SupplierForm
    model = Supplier

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        self.category = Category.objects.get(pk=self.get_object().category_id);
        context['category_name'] =  self.category.name
        context['parent_category_id'] = self.category.parent_id
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

def change_supplier_type(request):
    supplier_id = request.GET.get('supplier_id')
    type = request.GET.get('type')

    Supplier.objects.filter(pk=supplier_id).update(type=type)
    data = {
        'success': True
    }
    return JsonResponse(data)

 ## 2.2 Contact
  ### 2.2.1 ContactListView
class ContactListView(LoginRequiredMixin,ListView):
    model = Contact
    template_name = 'contact/contact_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        self.contact_active = Contact.objects.filter(supplier_id = supplier_id).exclude(type="Archived")
        self.contact_archived = Contact.objects.filter(supplier_id = supplier_id,type="Archived")
        return Contact.objects.filter(supplier_id = supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contact"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['contact_active'] = self.contact_active
        context['contact_archived'] = self.contact_archived
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
# class ContactDeleteView(LoginRequiredMixin,DeleteView):
#     model = Contact
#     template_name = 'contact/contact_confirm_delete.html'
#
#     def get_success_url(self):
#         return reverse_lazy('suppliers:contact_list', kwargs={'pk': Contact.objects.get(id=self.kwargs['pk']).supplier_id})
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contact"}
#         context['supplier'] = Supplier.objects.get(pk=Contact.objects.get(id=self.kwargs['pk']).supplier_id)
#         return context

  ### 2.2.5 View Functions for Contacts
def change_contact_type(request):
    contact_id = request.GET.get('contact_id')
    type = request.GET.get('type')

    Contact.objects.filter(pk=contact_id).update(type=type)
    data = {
        'success': True
    }
    return JsonResponse(data)


 ## 2.3 Bank
  ### 2.3.1 BankListView
class BankListView(LoginRequiredMixin,ListView):
    model = Bank
    template_name = 'bank/bank_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        self.bank_active = Bank.objects.filter(supplier_id = supplier_id,type="Active")
        self.bank_archived = Bank.objects.filter(supplier_id = supplier_id,type="Archived")
        return Bank.objects.filter(supplier_id = supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"bank"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['bank_active'] = self.bank_active
        context['bank_archived'] = self.bank_archived
        return context

  ### 2.3.2 BankDetailView
class BankDetailView(LoginRequiredMixin,DetailView):
    model = Bank
    template_name = 'bank/bank_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"bank"}
        context['supplier'] = Supplier.objects.get(pk=Bank.objects.get(pk=self.kwargs['pk']).supplier_id)
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
        self.contract_active = Contract.objects.filter(supplier_id = supplier_id,type="Active")
        self.contract_archived = Contract.objects.filter(supplier_id = supplier_id,type="Archived")
        return Contract.objects.filter(supplier_id = supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"contract"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['contract_active'] = self.contract_active
        context['contract_archived'] = self.contract_archived
        return context

  ### 2.4.2 CreateContractView
class CreateContractView(LoginRequiredMixin,CreateView):
    form_class = ContractForm
    model = Contract
    template_name = 'contract/contract_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        Contract.objects.all().update(type="Archived")
        self.object.title = "Contract-"+timezone.now().strftime("%Y%m%d")
        self.object.type = "Active"
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

  ### 2.2.5 View Functions for Contract
def change_contract_type(request):
    contract_id = request.GET.get('contract_id')
    type = request.GET.get('type')

    Contract.objects.filter(pk=contract_id).update(type=type)
    data = {
        'success': True
    }
    return JsonResponse(data)

 ## 2.5 ProductPrice
  ### 2.5.1 ProductPriceListView
class ProductPriceListView(LoginRequiredMixin,ListView):
    model = ProductPrice
    template_name = 'productprice/productprice_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        self.productprice_active = ProductPrice.objects.filter(supplier_id = supplier_id, type="Active", product__ean__isnull=False).exclude(product__ean='')
        self.productprice_archived = ProductPrice.objects.filter(supplier_id = supplier_id, type="Archived", product__ean__isnull=False).exclude(product__ean='')
        return ProductPrice.objects.filter(supplier_id = supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"product"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['productprice_active'] = self.productprice_active
        context['productprice_archived'] = self.productprice_archived
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
        context['products'] = Product.objects.filter(ean__isnull=False).exclude(ean='')
        context['currency'] = Currency.objects.all()
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

def add_pricelist(request):
    if request.method == 'POST':
        supplier_id = request.POST['supplier_id']
        supplier = Supplier.objects.get(pk=supplier_id)
        for product_id in request.POST.getlist('product_id'):
            if product_id:
                product = Product.objects.get(pk=product_id)
                currency = request.POST['currency'+product_id]
                currency_i = Currency.objects.get(pk=currency)
                price = request.POST['price'+product_id]
                if product and currency:
                    ProductPrice.objects.filter(supplier=supplier,product=product).update(type="Archived")
                    pricelist = ProductPrice(type="Active",supplier=supplier,product=product,currency=currency_i,price=price)
                    pricelist.save()
                for productbundle in ProductBundle.objects.filter(product=product):
                    product_bundle_id = productbundle.bundle_product_id
                    bundle_currency = request.POST['bcurrency'+str(product_bundle_id)]
                    bundle_currency_i = Currency.objects.get(pk=bundle_currency)
                    bundle_price = request.POST['bprice'+str(product_bundle_id)]
                    if bundle_price and currency:
                        ProductPrice.objects.filter(supplier=supplier,product_id=product_bundle_id).update(type="Archived")
                        bundle_pricelist = ProductPrice(type="Active",supplier=supplier,product_id=product_bundle_id,currency=bundle_currency_i,price=bundle_price,parent=pricelist)
                        bundle_pricelist.save()
    return redirect('suppliers:productprice_list', pk=supplier_id)

def change_pricelist_type(request):
    productprice_id = request.GET.get('productprice_id')
    type = request.GET.get('type')

    productprice = ProductPrice.objects.get(pk=productprice_id)
    if type == "Active":
        ProductPrice.objects.filter(product=productprice.product,supplier=productprice.supplier).update(type="Archived")
    ProductPrice.objects.filter(pk=productprice_id).update(type=type)
    data = {
        'success': True
    }
    return JsonResponse(data)
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
        products = Category.objects.get(name="Products")
        category = Category.objects.filter(parent=products.id)
        cat_data = '{"id":"'+str(products.id)+'","text":"'+products.name+'","children":['
        i=1
        for cat1 in category:
            if i!=1:
                cat_data += ','
            cat_data += '{"id":"'+str(cat1.id)+'","text":"'+cat1.name+'"'
            category2 = Category.objects.filter(parent=cat1.id)
            if category2:
                i2=1
                cat_data += ',"children":['
                for cat2 in category2:
                    if i2!=1:
                        cat_data += ','
                    cat_data += '{"id":"'+str(cat2.id)+'","text":"'+cat2.name+'"'
                    category3 = Category.objects.filter(parent=cat2.id)
                    if category3:
                        i3=1
                        cat_data += ',"children":['
                        for cat3 in category3:
                            if i3!=1:
                                cat_data += ','
                            cat_data += '{"id":"'+str(cat3.id)+'","text":"'+cat3.name+'"'
                            category4 = Category.objects.filter(parent=cat3.id)
                            if category4:
                                i4=1
                                cat_data += ',"children":['
                                for cat4 in category4:
                                    if i4!=1:
                                        cat_data += ','
                                    cat_data += '{"id":"'+str(cat4.id)+'","text":"'+cat4.name+'"'
                                    cat_data += "}"
                                    i4 = i4+1
                                cat_data += ']'
                            cat_data += "}"
                            i3 = i3+1
                        cat_data += ']'
                    cat_data += "}"
                    i2 = i2+1
                cat_data += ']'
            cat_data += "}"
            i = i+1
        cat_data += ']}'
        context['cat_data'] = cat_data
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
        self.mold = Mold.objects.get(id=self.kwargs['pk'])
        context['supplier'] = Supplier.objects.get(pk=self.mold.supplier_id)
        categories = self.mold.category.all()
        category_list = []
        for category in categories:
            category_list.append(str(category.pk))
        category_list = ",".join(category_list)
        context['category_list'] = category_list
        context['paid_by'] = self.mold.paid_by
        products = Category.objects.get(name="Products")
        category = Category.objects.filter(parent=products.id)
        cat_data = '{"id":"'+str(products.id)+'","text":"'+products.name+'","children":['
        i=1
        for cat1 in category:
            if i!=1:
                cat_data += ','
            cat_data += '{"id":"'+str(cat1.id)+'","text":"'+cat1.name+'"'
            category2 = Category.objects.filter(parent=cat1.id)
            if category2:
                i2=1
                cat_data += ',"children":['
                for cat2 in category2:
                    if i2!=1:
                        cat_data += ','
                    cat_data += '{"id":"'+str(cat2.id)+'","text":"'+cat2.name+'"'
                    category3 = Category.objects.filter(parent=cat2.id)
                    if category3:
                        i3=1
                        cat_data += ',"children":['
                        for cat3 in category3:
                            if i3!=1:
                                cat_data += ','
                            cat_data += '{"id":"'+str(cat3.id)+'","text":"'+cat3.name+'"'
                            category4 = Category.objects.filter(parent=cat3.id)
                            if category4:
                                i4=1
                                cat_data += ',"children":['
                                for cat4 in category4:
                                    if i4!=1:
                                        cat_data += ','
                                    cat_data += '{"id":"'+str(cat4.id)+'","text":"'+cat4.name+'"'
                                    cat_data += "}"
                                    i4 = i4+1
                                cat_data += ']'
                            cat_data += "}"
                            i3 = i3+1
                        cat_data += ']'
                    cat_data += "}"
                    i2 = i2+1
                cat_data += ']'
            cat_data += "}"
            i = i+1
        cat_data += ']}'
        context['cat_data'] = cat_data
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
        self.moldfile_active = MoldFile.objects.filter(mold_id = mold_id,type="Active")
        self.moldfile_archived = MoldFile.objects.filter(mold_id = mold_id,type="Archived")
        return MoldFile.objects.filter(mold_id = mold_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"file"}
        context['mold_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['mold'] = self.mold
        context['moldfile_active'] = self.moldfile_active
        context['moldfile_archived'] = self.moldfile_archived
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
        MoldFile.objects.filter(mold=self.object.mold.pk).update(type="Archived")
        self.object.type = "Active"
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

  ### 2.6.3 MoldHost
   #### 2.6.3.1 MoldHostListView
class MoldHostListView(LoginRequiredMixin,ListView):
    model = MoldHost
    template_name = 'moldhost/moldhost_list.html'

    def get_queryset(self):
        mold_id = self.kwargs['pk']
        self.mold = Mold.objects.get(pk=mold_id)
        self.supplier = Supplier.objects.get(pk=self.mold.supplier_id)
        self.moldhost_active = MoldHost.objects.filter(mold_id = mold_id,type="Active")
        self.moldhost_archived = MoldHost.objects.filter(mold_id = mold_id,type="Archived")
        return MoldHost.objects.filter(mold_id = mold_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"host"}
        context['mold_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['mold'] = self.mold
        context['moldhost_active'] = self.moldhost_active
        context['moldhost_archived'] = self.moldhost_archived
        return context

   #### 2.6.2.2 CreateMoldFileView
 ### not using query_set here because it don't work with createview
class CreateMoldHostView(LoginRequiredMixin,CreateView):
    form_class = MoldHostForm
    model = MoldHost
    template_name = 'moldhost/moldhost_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.mold = Mold.objects.get(id=self.kwargs['pk'])
        MoldHost.objects.filter(mold=self.object.mold.pk).update(type="Archived")
        self.object.type = "Active"
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"host"}
        mold_id = self.kwargs['pk']
        self.mold = Mold.objects.get(pk=mold_id)
        self.supplier = Supplier.objects.get(pk=self.mold.supplier_id)
        context['supplier'] = self.supplier
        context['mold'] = self.mold

        return context

   #### 2.6.2.3 MoldHostUpdateView
class MoldHostUpdateView(LoginRequiredMixin,UpdateView):
    form_class = MoldHostForm
    model = MoldHost
    template_name = 'moldhost/moldhost_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"host"}
        moldfile_id = self.kwargs['pk']
        self.mold = Mold.objects.get(pk=MoldHost.objects.get(id=moldhost_id).mold_id)
        self.supplier = Supplier.objects.get(pk=self.mold.supplier_id)
        context['supplier'] = self.supplier
        context['mold'] = self.mold
        return context

   #### 2.6.2.4 MoldHostDeleteView
class MoldHostDeleteView(LoginRequiredMixin,DeleteView):
    model = MoldHost
    template_name = 'moldhost/moldhost_confirm_delete.html'

    def get_queryset(self):
        moldhost_id = self.kwargs['pk']
        self.mold = Mold.objects.get(pk=MoldHost.objects.get(id=moldhost_id).mold_id)
        self.supplier = Supplier.objects.get(pk=self.mold.supplier_id)
        return MoldHost.objects.filter(pk=moldhost_id)

    def get_success_url(self):
        return reverse_lazy('suppliers:moldhost_list', kwargs={'pk': MoldHost.objects.get(id=self.kwargs['pk']).mold_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"host"}
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
        self.aql_active = Aql.objects.filter(type="Active")
        self.aql_archived = Aql.objects.filter(type="Archived")
        return Aql.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"me","menu4":"aql"}
        context['aql_active'] = self.aql_active
        context['aql_archived'] = self.aql_archived
        return context

   #### 2.7.1.2 AqlDetailView
class AqlDetailView(LoginRequiredMixin,DetailView):
    model = Aql
    template_name = 'aql/aql_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"me","menu4":"aql","menu5":"detail"}
        return context

   #### 2.7.1.3 CreateAqlView
class CreateAqlView(LoginRequiredMixin,CreateView):
    form_class = AqlForm
    model = Aql
    template_name = 'aql/aql_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        Aql.objects.filter(category_id=self.object.category).update(type="Archived")
        aql_version = 1
        if Aql.objects.filter(category_id=self.object.category).exists():
            aql_q = Aql.objects.filter(category_id=self.object.category).order_by('-version')[:1].get()
            aql_version = aql_q.version + 0.1
        self.object.version = aql_version
        self.object.type = "Active"
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"me","menu4":"aql"}
        context['parent_category_id'] = Category.objects.get(name__exact=CAT_PRODUCT).pk
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
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"me","menu4":"aql"}
        return context

   #### 2.7.1.5 AqlDeleteView
class AqlDeleteView(LoginRequiredMixin,DeleteView):
    model = Aql
    template_name = 'aql/aql_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:aql_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"aql"}
        return context

    #### 2.7.1.6 Function for AQL
def change_aql_type(request):
    aql_id = request.GET.get('aql_id')
    type = request.GET.get('type')
    aql = Aql.objects.get(pk=aql_id)

    if type == "Active":
        Aql.objects.filter(category=aql.category).update(type="Archived")
    Aql.objects.filter(pk=aql_id).update(type=type)
    data = {
        'success': True
    }
    return JsonResponse(data)
 ## 2.8 Order
  ### 2.8.1 Order
   #### 2.8.1.1 OrderListView
class OrderListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'order/active_order_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        self.orders = Order.objects.filter(supplier_id=supplier_id, status__title="Active").order_by('-pk')
        self.active_orders = []
        for order in self.orders:
            active_order1 = {}
            active_order1["pk"] = order.pk
            active_order1["amount"] = int(order.amount)
            active_order1["currency"] = order.currency
            active_order1["quantity"] = order.quantity
            active_order1["paid_amount"] = OrderPayment.objects.filter(order=order,status__title="Paid").aggregate(Sum('invoice_amount'))
            active_order1["paid_amount"] = active_order1["paid_amount"]["invoice_amount__sum"]
            if active_order1["paid_amount"]:
                active_order1["paid_amount"] = int(active_order1["paid_amount"])
            else:
                active_order1["paid_amount"] = 0
            active_order1["amount_percentage"] = (Decimal(active_order1["paid_amount"])*Decimal(100))/Decimal(active_order1["amount"])
            active_order1["quantity_send"] = OrderDelivery.objects.filter(order=order,date__lt=datetime.now()).aggregate(Sum('quantity'))
            active_order1["quantity_send"] = active_order1["quantity_send"]["quantity__sum"]
            if active_order1["quantity_send"]:
                active_order1["quantity_percentage"] = (int(active_order1["quantity_send"])*int(100))/int(active_order1["quantity"])
            else:
                active_order1["quantity_percentage"] = 0
                active_order1["quantity_send"] = 0

            active_order1["products"] = []

            for orderproduct in order.orderproduct_set.all():
                order_product = {}
                order_product["title"] = orderproduct.productprice.product.title
                order_product["image"] = orderproduct.productprice.product.image
                order_product["ean"] = orderproduct.productprice.product.ean
                order_product["price"] = orderproduct.productprice.price
                order_product["currency"] = orderproduct.productprice.currency
                order_product["quantity"] = orderproduct.quantity
                order_product["quantity_send"] = OrderDeliveryProduct.objects.filter(orderdelivery__order=order, orderproduct=orderproduct, orderdelivery__date__lt=datetime.now()).aggregate(Sum('quantity'))
                order_product["quantity_send"] = order_product["quantity_send"]["quantity__sum"]
                if order_product["quantity_send"]:
                    order_product["quantity_percentage"] = (int(order_product["quantity_send"])*int(100))/int(order_product["quantity"])
                else:
                    order_product["quantity_percentage"] = 0
                    order_product["quantity_send"] = 0

                active_order1["products"].append(order_product)

            self.active_orders.append(active_order1)
        logger.warning(self.active_orders)
        return Order.objects.filter(supplier_id=supplier_id, status__title="Active").order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"active"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['active_orders'] = self.active_orders
        return context

   #### 2.8.1.2 PendingPOListView
class PendingPOListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'order/pending_po_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        self.pending_pos = Order.objects.filter(supplier_id=supplier_id, status__title="Pending PO").order_by('-pk')
        self.awaiting_pis = Order.objects.filter(supplier_id=supplier_id, status__title="Awaiting PI").order_by('-pk')
        return Order.objects.filter(supplier_id=supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"pending"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['pending_pos'] = self.pending_pos
        context['awaiting_pis'] = self.awaiting_pis
        return context

   #### 2.8.1.3 ClosedOrderListView
class ClosedOrderListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'order/closed_order_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        self.pending_pos = Order.objects.filter(supplier_id=supplier_id, status__title="Pending PO").order_by('-pk')
        self.awaiting_pis = Order.objects.filter(supplier_id=supplier_id, status__title="Awaiting PI").order_by('-pk')
        return Order.objects.filter(supplier_id=supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"closed"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['pending_pos'] = self.pending_pos
        context['awaiting_pis'] = self.awaiting_pis
        return context

   #### 2.8.1.3 CompletedOrderListView
class CompletedOrderListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'order/completed_order_list.html'

    def get_queryset(self):
        supplier_id = self.kwargs['pk']
        self.supplier = Supplier.objects.get(pk=supplier_id)
        self.pending_pos = Order.objects.filter(supplier_id=supplier_id, status__title="Pending PO").order_by('-pk')
        self.awaiting_pis = Order.objects.filter(supplier_id=supplier_id, status__title="Awaiting PI").order_by('-pk')
        return Order.objects.filter(supplier_id=supplier_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"completed"}
        context['supplier_id'] = self.kwargs['pk']
        context['supplier'] = self.supplier
        context['pending_pos'] = self.pending_pos
        context['awaiting_pis'] = self.awaiting_pis
        return context

   #### 2.8.1.2 OrderDetailView
class OrderDetailView(LoginRequiredMixin,DetailView):
    model = Order
    template_name = 'order/order_detail.html'

    def get_queryset(self):
        order_id = self.kwargs['pk']
        self.orderpayments = OrderPayment.objects.filter(order_id=order_id).order_by('date')
        self.orderdeliveries = OrderDelivery.objects.filter(order_id=order_id).order_by('date')
        self.company = CompanySetting.objects.all().first()
        self.currency = Currency.objects.all()
        if OrderFile.objects.filter(order_id=order_id,title="PI").exists():
            self.order_pi = OrderFile.objects.get(order_id=order_id,title="PI").file_url
        else:
            self.order_pi = ""
        status_title = Order.objects.get(pk=order_id).status.title
        if status_title == "Pending PO" or status_title == "Awaiting PI" or status_title == "PI Confirm":
            self.order_class = ""
        else:
            self.order_class = "collapse"
        remaining_quantity = OrderProduct.objects.filter(order_id=order_id).aggregate(Sum('remaining_quantity'))
        self.remaining_quantity = remaining_quantity["remaining_quantity__sum"]
        self.test_status = Status.objects.filter(parent_id=Status.objects.get(title__exact='Test Report'))
        return Order.objects.filter(pk=order_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"detail"}
        context['supplier'] = Supplier.objects.get(pk=Order.objects.get(pk=self.kwargs['pk']).supplier_id)
        context['orderpayments'] = self.orderpayments
        context['orderdeliveries'] = self.orderdeliveries
        context['company'] = self.company
        context['all_currency'] = self.currency
        context['order_class'] = self.order_class
        context['order_pi'] = self.order_pi
        context['test_status'] = self.test_status
        context['remaining_quantity'] = self.remaining_quantity
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
        context['paymentterms'] = PaymentTerms.objects.all()
        context['contacts'] = Contact.objects.filter(supplier_id=self.kwargs['pk']).exclude(type="Archived")
        context['productprice'] = ProductPrice.objects.filter(supplier_id=self.kwargs['pk'], product__ean__isnull=False, type="Active").exclude(product__ean='')
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
        return reverse_lazy('suppliers:active_order_list', kwargs={'pk': Order.objects.get(pk=self.kwargs['pk']).supplier_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order"}
        context['supplier'] = Supplier.objects.get(pk=Order.objects.get(pk=self.kwargs['pk']).supplier_id)
        return context

   #### 2.8.1.6 View function for Order
def generate_po(request):
    if request.method == 'POST':
        supplier_id = request.POST['supplier_id']
        supplier = Supplier.objects.get(pk=supplier_id)
        batch_id = supplier.name[:3].upper()+""+timezone.now().strftime("%d%m%Y")
        contact_id = request.POST.get('contact_id',False)
        products_id = request.POST.getlist('product_id')
        if contact_id and products_id:
            contact = Contact.objects.get(pk=contact_id)
            user = request.user
            order_status = Status.objects.get(title= "Orders", parent__isnull=True)
            status = Status.objects.get(title="Pending PO", parent=order_status)
            if contact and user:
                order = Order(supplier=supplier,user=user,contact=contact,status=status,batch_id=batch_id)
                order.save()
                total_amount = 0
                total_quantity = 0
                currency = ""
                for product_id in products_id:
                    if product_id:
                        productprice = ProductPrice.objects.get(pk=product_id)
                        quantity = request.POST['quantity'+product_id]
                        paymentterm_id = request.POST['paymentterm'+product_id]
                        paymentterm = PaymentTerms.objects.get(pk=paymentterm_id)
                        aql = Aql.objects.get(category_id=productprice.product.category,type="Active")
                        if productprice and quantity:
                            orderproduct = OrderProduct(order=order,productprice=productprice,quantity=quantity,aql=aql,paymentterms=paymentterm,remaining_quantity=quantity)
                            orderproduct.save()
                            total_amount = Decimal(total_amount)+(Decimal(quantity)*(productprice.price))
                            total_quantity = int(total_quantity)+int(quantity)
                            currency = productprice.currency
                order.amount = total_amount
                order.quantity = total_quantity
                order.currency = currency
                orderproducts = OrderProduct.objects.filter(order_id=order.pk)
                total_deposit_amount = 0
                for orderproduct in orderproducts:
                    deposit = orderproduct.paymentterms.deposit
                    price = orderproduct.productprice.price
                    quantity = orderproduct.quantity
                    if deposit:
                        deposit_amount = (Decimal(deposit)*Decimal(price)*Decimal(quantity))/Decimal(100)
                    else:
                        deposit_amount = 0
                    total_deposit_amount = total_deposit_amount+deposit_amount
                order.deposit_amount = total_deposit_amount
                order.save()

            html_template = render_to_string('order/pdf_file.html',{'order':order,'company':CompanySetting.objects.all().first()})
            file_name = "order-"+slugify(supplier.name)+"-po-"+timezone.now().strftime("%Y%m%d")+".pdf";
            os.makedirs("project_content/suppliers/"+str(supplier_id)+"/Orders/"+str(order.pk)+"/", exist_ok=True)
            pdf_file = HTML(string=html_template,base_url=request.build_absolute_uri()).write_pdf("project_content/suppliers/"+str(supplier_id)+"/Orders/"+str(order.pk)+"/"+file_name)
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = 'filename="'+file_name+'"'
            file_path = "suppliers/"+str(supplier_id)+"/Orders/"+str(order.pk)+"/"+file_name
            orderfile = OrderFile(title="PO",file_url=file_path,order=order)
            orderfile.save()
        else:
            if not contact_id:
                contact_error = "Please select supplier contact"
                messages.error(request, contact_error)
            if not products_id:
                product_error = "Please select atleast one product to generate PO"
                messages.error(request, product_error)
            return redirect('suppliers:create_order',pk=supplier_id)
    return redirect('suppliers:pending_po_list', pk=supplier_id)

def confirm_po(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order_status = Status.objects.get(title= "Orders", parent__isnull=True)
        status = Status.objects.get(title = "Awaiting PI", parent=order_status)
        supplier_id = Order.objects.get(pk=order_id).supplier_id
        Order.objects.filter(pk=order_id).update(status=status)
    return redirect('suppliers:order_detail', pk=order_id)

def awaiting_pi(request):
    if request.method == 'POST':
        order_id = request.POST['order']
        order_file_id = request.POST.get('order_file',False)
        form = OrderFileForm(request.POST, request.FILES)
        if form.is_valid():
            if order_file_id:
                order_file = OrderFile.objects.get(pk=order_file_id)
                order_file.file_url = request.FILES['file_url']
                order_file.save()
            else:
                form.save()
                deposit_receipt = OrderFile(title="Deposit",order_id=order_id,file_url=request.FILES['deposit_receipt'])
                deposit_receipt.save()
                order_status = Status.objects.get(title= "Orders", parent__isnull=True)
                status = Status.objects.get(title = "PI Confirm", parent=order_status)
                Order.objects.filter(pk=order_id).update(status=status)
            return redirect('suppliers:order_detail', pk=order_id)
    else:
        form = OrderFileForm()
    return redirect('suppliers:order_detail', pk=order_id)

def activate_order(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order_status = Status.objects.get(title= "Orders", parent__isnull=True)
        status = Status.objects.get(title = "Active", parent=order_status)
        order = Order.objects.get(pk=order_id)
        supplier_id = order.supplier_id
        Order.objects.filter(pk=order_id).update(status=status)

        orderproducts = OrderProduct.objects.filter(order_id=order_id)
        total_deposit_amount = 0
        for orderproduct in orderproducts:
            deposit = orderproduct.paymentterms.deposit
            price = orderproduct.productprice.price
            quantity = orderproduct.quantity
            if deposit:
                deposit_amount = (Decimal(deposit)*Decimal(price)*Decimal(quantity))/Decimal(100)
            else:
                deposit_amount = 0
            total_deposit_amount = total_deposit_amount+deposit_amount

        bank = Bank.objects.filter(supplier_id=supplier_id,type="Active").first()
        payment_status = Status.objects.get(title= "Payments", parent__isnull=True)
        status = Status.objects.get(title="Paid", parent=payment_status)
        share_percentage = round((Decimal(total_deposit_amount)*Decimal(100))/Decimal(order.amount))
        orderpayment = OrderPayment(order=order,bank=bank,paid_amount=total_deposit_amount,invoice_amount=total_deposit_amount,date=timezone.now(),invoice_currency=order.currency,paid_currency=order.currency,status=status,share_percentage=share_percentage)
        orderpayment.save()
    return redirect('suppliers:order_detail', pk=order_id)

def add_orderdelivery(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order = Order.objects.get(pk=order_id)
        d_date = request.POST.get('date',False)
        products_id = request.POST.getlist('product_id')
        if d_date and products_id:
            date = datetime.strptime(d_date,"%m/%d/%Y").date()
            delivery_status = Status.objects.get(title= "Partial Delivery", parent__isnull=True)
            status = Status.objects.get(title = "Schedule", parent=delivery_status)
            batch_id_count = OrderDelivery.objects.filter(order=order).count()
            batch_id = order.batch_id+"-"+str(batch_id_count+1)
            if date:
                orderdelivery = OrderDelivery(order=order, date=date, status=status, batch_id=batch_id)
                orderdelivery.save()
                total_quantity = 0
                total_amount_ondelivery = 0
                total_amount_remaining = 0
                paymentlist = {}
                for product_id in products_id:
                    if product_id:
                        quantity = request.POST['quantity'+product_id].replace(',','')
                        orderproduct = OrderProduct.objects.get(pk=product_id)
                        share_percentage = round((Decimal(quantity)*Decimal(100))/Decimal(order.quantity))
                        orderdeliveryproduct = OrderDeliveryProduct(orderdelivery=orderdelivery,orderproduct=orderproduct,quantity=quantity,share_percentage=share_percentage)
                        orderdeliveryproduct.save()
                        orderproduct.remaining_quantity = int(orderproduct.remaining_quantity)-int(quantity)
                        orderproduct.save()
                        productprice_price = orderdeliveryproduct.orderproduct.productprice.price
                        paymentterm_deposit = orderdeliveryproduct.orderproduct.paymentterms.deposit
                        paymentterm_days = orderdeliveryproduct.orderproduct.paymentterms.payment_term
                        paymentterm_ondelivery = orderdeliveryproduct.orderproduct.paymentterms.on_delivery
                        paymentterm_remaining = 100-(paymentterm_ondelivery+paymentterm_deposit)
                        amount_ondelivery = (Decimal(quantity)*Decimal(productprice_price)*Decimal(paymentterm_ondelivery))/Decimal(100)
                        amount_remaining = (Decimal(quantity)*Decimal(productprice_price)*Decimal(paymentterm_remaining))/Decimal(100)

                        total_quantity = total_quantity+int(quantity)
                        if paymentterm_days in paymentlist:
                            paymentlist[paymentterm_days] += amount_remaining
                        else:
                            paymentlist[paymentterm_days] = amount_remaining
                        total_amount_ondelivery = total_amount_ondelivery+int(amount_ondelivery)
                share_percentage = round((Decimal(total_quantity)*Decimal(100))/Decimal(order.quantity))
                orderdelivery.quantity = total_quantity
                orderdelivery.share_percentage = share_percentage
                orderdelivery.save()
            bank = Bank.objects.filter(supplier_id=order.supplier_id,type="Active").first()
            if total_amount_ondelivery:
                payment_status = Status.objects.get(title= "Payments", parent__isnull=True)
                status = Status.objects.get(title="Pending", parent=payment_status)
                share_percentage = round((Decimal(total_amount_ondelivery)*Decimal(100))/Decimal(order.amount))
                orderpayment = OrderPayment(order=order,bank=bank,paid_amount=total_amount_ondelivery,invoice_amount=total_amount_ondelivery,date=date,invoice_currency=order.currency,paid_currency=order.currency,status=status,orderdelivery=orderdelivery,share_percentage=share_percentage)
                orderpayment.save()

            payment_status = Status.objects.get(title= "Payments", parent__isnull=True)
            status = Status.objects.get(title="Schedule", parent=payment_status)

            for days in paymentlist:
                if paymentlist[days]:
                    date = date + timedelta(days=days)
                    share_percentage = round((Decimal(paymentlist[days])*Decimal(100))/Decimal(order.amount))
                    orderpayment = OrderPayment(order=order,bank=bank,paid_amount=paymentlist[days],invoice_amount=paymentlist[days],date=date,invoice_currency=order.currency,paid_currency=order.currency,status=status,orderdelivery=orderdelivery,share_percentage=share_percentage)
                    orderpayment.save()
        else:
            if not d_date:
                date_error = "Please select delivery date"
                messages.error(request, date_error)
            if not products_id:
                product_error = "Please select atleast one product to create delivery"
                messages.error(request, product_error)
            return redirect('suppliers:create_orderdelivery',pk=order_id)

    return redirect('suppliers:order_detail', pk=order_id)

def update_deliverydate(request):
    if request.method == 'POST':
        orderdelivery_id = request.POST['orderdelivery_id']
        orderdelivery = OrderDelivery.objects.get(pk=orderdelivery_id)
        order_id = orderdelivery.order_id
        old_date = orderdelivery.date.date()
        new_date = datetime.strptime(request.POST['date'],"%m/%d/%Y").date()
        days = (new_date - old_date).days

        orderdelivery.date = new_date
        orderdelivery.save()

        orderpayments = OrderPayment.objects.filter(orderdelivery=orderdelivery)
        for orderpayment in orderpayments:
            orderpayment.date = orderpayment.date + timedelta(days=days)
            orderpayment.save()

    return redirect('suppliers:order_detail', pk=order_id)

def update_deliverypayment(request):
    if request.method == 'POST':
        orderpayment_id = request.POST['orderpayment_id']
        currency_id = request.POST['currency']
        price = request.POST['price']
        orderpayment = OrderPayment.objects.get(pk=orderpayment_id)
        order_id = orderpayment.order_id
        orderpayment.paid_currency_id=currency_id
        orderpayment.paid_amount = price

        payment_status = Status.objects.get(title= "Payments", parent__isnull=True)
        status = Status.objects.get(title="Paid", parent=payment_status)
        orderpayment.status = status
        orderpayment.pi_file = request.FILES['pi_file']
        orderpayment.receipt_file = request.FILES['receipt_file']
        orderpayment.save()
    return redirect('suppliers:order_detail', pk=order_id)

def submit_test_report(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id',False)
        deliveryproduct_id = request.POST.get('deliveryproduct_id',False)
        status = request.POST.get('status',False)
        test_report_file = request.FILES['test_file']
        note = request.POST.get('note',False)
        if deliveryproduct_id and status and test_report_file and note:
            test_report = OrderDeliveryTestReport(orderdeliveryproduct_id=deliveryproduct_id, test_report=test_report_file, status_id=status, note=note)
            test_report.save()
            deliveryproduct = OrderDeliveryProduct.objects.get(pk=deliveryproduct_id)
            deliveryproduct.status_id = status
            deliveryproduct.save()
            if Status.objects.get(pk=status).title == "Accept":
                delivery = OrderDelivery.objects.get(pk=deliveryproduct.orderdelivery_id)
                delivery_status = Status.objects.get(title= "Partial Delivery", parent__isnull=True)
                d_status = Status.objects.get(title="Ready To Ship", parent=delivery_status)
                delivery.status = d_status
                delivery.save()
    return redirect('suppliers:order_detail', pk=order_id)

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
        self.supplier = Supplier.objects.get(pk=self.order.supplier_id)
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
        self.supplier = Supplier.objects.get(pk=self.order.supplier_id)
        return OrderFile.objects.filter(pk=orderfile_id)

    def get_success_url(self):
        return reverse_lazy('suppliers:order_detail', kwargs={'pk': OrderFile.objects.get(id=self.kwargs['pk']).order_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"order","menu5":"detail"}
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
        self.supplier = Supplier.objects.get(pk=self.order.supplier_id)
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
        self.supplier = Supplier.objects.get(pk=self.order.supplier_id)
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
        self.supplier = Supplier.objects.get(pk=self.order.supplier_id)
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
        self.supplier = Supplier.objects.get(pk=self.order.supplier_id)
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
        self.supplier = Supplier.objects.get(pk=self.order.supplier_id)
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
        self.supplier = Supplier.objects.get(pk=self.order.supplier_id)
        context['supplier'] = self.supplier
        context['order'] = self.order
        context['orderproducts'] = OrderProduct.objects.filter(order_id=order_id)
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

# 3. Certification
 ## 3.1 CertificationListView
class CertificationListView(LoginRequiredMixin,ListView):
    model = Certification
    template_name = 'certification/certification_list.html'

    def get_queryset(self):
        self.certification_active = Certification.objects.filter(type="Active")
        self.certification_archived = Certification.objects.filter(type="Archived")
        return Certification.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"certification"}
        context['certification_active'] = self.certification_active
        context['certification_archived'] = self.certification_archived
        return context

 ## 1.2 CreateCertificationView
class CreateCertificationView(LoginRequiredMixin,CreateView):
    form_class = CertificationForm
    model = Certification
    template_name = 'certification/certification_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.type = "Active"
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"certification"}
        return context

 ## 1.3 CertificationUpdateView
class CertificationUpdateView(LoginRequiredMixin,UpdateView):
    form_class = CertificationForm
    model = Certification
    template_name = 'certification/certification_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"certification"}
        return context

 ## 1.4 CertificationDeleteView
class CertificationDeleteView(LoginRequiredMixin,DeleteView):
    model = Certification
    template_name = 'certification/certification_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:certification_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"certification"}
        return context

 ## 1.5 Function for Certification
def change_certification_type(request):
    certification_id = request.GET.get('certification_id')
    type = request.GET.get('type')

    Certification.objects.filter(pk=certification_id).update(type=type)
    data = {
        'success': True
    }
    return JsonResponse(data)
