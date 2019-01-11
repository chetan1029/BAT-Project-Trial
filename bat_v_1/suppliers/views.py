from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.urls import reverse_lazy
from suppliers.models import (Supplier, Category, PaymentTerms, Status, Contact,
                              Currency, Bank, Contract, ProductPrice, Mold)
from suppliers.forms import (SupplierForm, CategoryForm, PaymentTermsForm, StatusForm, ContactForm,
                              CurrencyForm, BankForm, ContractForm, ProductPriceForm, MoldForm)
from django.db.models import Q
# Create your views here.
# 1. Supplier
 ## 1.1 SupplierListView
 ## 1.2 SupplierDetailView
 ## 1.3 CreateSupplierView
 ## 1.4 SupplierUpdateView
 ## 1.5 SupplierDeleteView
# 2. Category
 ## 2.1 CategoryListView
 ## 2.2 CreateCategoryView
 ## 2.3 CategoryUpdateView
 ## 2.4 CategoryDeleteView
# 3. Payment Terms
 ## 3.1 PaymentTermsListView
 ## 3.2 CreatePaymentTermsView
 ## 3.3 PaymentTermsUpdateView
 ## 3.4 PaymentTermsDeleteView
# 4. Status
 ## 4.1 StatusListView
 ## 4.2 CreateStatusView
 ## 4.3 StatusUpdateView
 ## 4.4 StatusDeleteView
# 5. Contact
 ## 5.1 ContactListView
 ## 5.2 CreateContactView
 ## 5.3 ContactUpdateView
 ## 5.4 ContactDeleteView
# 6. Currecy
 ## 6.1 CurrecyListView
 ## 6.2 CreateCurrecyView
 ## 6.3 CurrecyUpdateView
 ## 6.4 CurrecyDeleteView
# 7. Bank
 ## 7.1 BankListView
 ## 7.2 BankDetailView
 ## 7.3 CreateBankView
 ## 7.4 BankUpdateView
 ## 7.5 BankDeleteView
# 8. Contract
 ## 8.1 ContractListView
 ## 8.2 CreateContractView
 ## 8.3 ContractUpdateView
 ## 8.4 ContractDeleteView
# 9. ProductPrice
 ## 9.1 ProductPriceListView
 ## 9.2 CreateProductPriceView
 ## 9.3 ProductPriceUpdateView
 ## 9.4 ProductPriceDeleteView
# 10. Mold
 ## 10.1 MoldListView
 ## 10.2 MoldDetailView
 ## 10.3 CreateMoldView
 ## 10.4 MoldUpdateView
 ## 10.5 MoldDeleteView
# 11. MoldProduct
 ## 11.1 MoldProductListView
 ## 11.2 CreateMoldProductView
 ## 11.3 MoldProductUpdateView
 ## 11.4 MoldProductDeleteView

# 1. Supplier
 ## 1.1 SupplierListView
class SupplierListView(LoginRequiredMixin,ListView):
    model = Supplier
    paginate_by = 10

    def get_queryset(self):
        self.order_by = self.request.GET.get('order_by', self.queryset)
        if self.order_by is None:
            self.order_by = "-create_date"

        self.search_q = self.request.GET.get('search_q', self.queryset)
        if self.search_q is None:
            queryset = Supplier.objects.all().order_by(self.order_by)
        else:
            queryset = Supplier.objects.filter(name__icontains=self.search_q)
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

 ## 1.2 SupplierDetailView
class SupplierDetailView(LoginRequiredMixin,DetailView):
    model = Supplier

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"details"}
        context['pk'] = self.kwargs['pk']
        return context

 ## 1.3 CreateSupplierView
class CreateSupplierView(LoginRequiredMixin,CreateView):
    form_class = SupplierForm
    model = Supplier

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        return context

 ## 1.4 SupplierUpdateView
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
        return context

 ## 1.5 SupplierDeleteView
class SupplierDeleteView(LoginRequiredMixin,DeleteView):
    model = Supplier
    success_url = reverse_lazy('suppliers:supplier_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers"}
        return context

# 2. Category
 ## 2.1 CategoryListView
class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'category/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"category"}
        return context

 ## 2.2 CreateCategoryView
class CreateCategoryView(LoginRequiredMixin,CreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'category/category_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"category"}
        return context

 ## 2.3 CategoryUpdateView
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
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"category"}
        return context

 ## 2.4 CategoryDeleteView
class CategoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"category"}
        return context

# 3. Payment Terms
 ## 3.1 PaymentTermsListView
class PaymentTermsListView(LoginRequiredMixin,ListView):
    model = PaymentTerms
    template_name = 'paymentterms/paymentterms_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"paymentterms"}
        return context

 ## 3.2 CreatePaymentTermsView
class CreatePaymentTermsView(LoginRequiredMixin,CreateView):
    form_class = PaymentTermsForm
    model = PaymentTerms
    template_name = 'paymentterms/paymentterms_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"paymentterms"}
        return context

 ## 3.3 PaymentTermsUpdateView
class PaymentTermsUpdateView(LoginRequiredMixin,UpdateView):
    form_class = PaymentTermsForm
    model = PaymentTerms
    template_name = 'paymentterms/paymentterms_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"paymentterms"}
        return context

 ## 3.4 PaymentTermsDeleteView
class PaymentTermsDeleteView(LoginRequiredMixin,DeleteView):
    model = PaymentTerms
    template_name = 'paymentterms/paymentterms_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:paymentterms_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"paymentterms"}
        return context

# 4. Status
 ## 4.1 StatusListView
class StatusListView(LoginRequiredMixin,ListView):
    model = Status
    template_name = 'status/status_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"status"}
        return context

 ## 4.2 CreateStatusView
class CreateStatusView(LoginRequiredMixin,CreateView):
    form_class = StatusForm
    model = Status
    template_name = 'status/status_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"status"}
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
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"status"}
        return context

 ## 4.4 StatusDeleteView
class StatusDeleteView(LoginRequiredMixin,DeleteView):
    model = Status
    template_name = 'status/status_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:status_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"status"}
        return context

# 5. Contact
 ## 5.1 ContactListView
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

 ## 5.2 CreateContactView
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

 ## 5.3 ContactUpdateView
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

 ## 5.4 ContactDeleteView
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

# 6. Currency
 ## 6.1 CurrencyListView
class CurrencyListView(LoginRequiredMixin,ListView):
    model = Currency
    template_name = 'currency/currency_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"currency"}
        return context

 ## 6.2 CreateCurrencyView
class CreateCurrencyView(LoginRequiredMixin,CreateView):
    form_class = CurrencyForm
    model = Currency
    template_name = 'currency/currency_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"currency"}
        return context

 ## 6.3 CurrencyUpdateView
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
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"currency"}
        return context

 ## 6.4 CurrencyDeleteView
class CurrencyDeleteView(LoginRequiredMixin,DeleteView):
    model = Currency
    template_name = 'currency/currency_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('suppliers:currency_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"currency"}
        return context

# 7. Bank
 ## 7.1 BankListView
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

 ## 7.2 BankDetailView
class BankDetailView(LoginRequiredMixin,DetailView):
    model = Bank
    template_name = 'bank/bank_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"bank"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        return context

 ## 7.3 CreateBankView
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

 ## 7.4 BankUpdateView
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

 ## 7.5 BankDeleteView
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

# 8. Contract
 ## 8.1 ContractListView
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

 ## 8.2 CreateContractView
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

 ## 8.3 ContractUpdateView
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

 ## 8.4 ContractDeleteView
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

# 9. ProductPrice
 ## 9.1 ProductPriceListView
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

 ## 9.2 CreateProductPriceView
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

 ## 9.3 ProductPriceUpdateView
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

 ## 9.4 ProductPriceDeleteView
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

# 10. Mold
 ## 10.1 MoldListView
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

 ## 10.2 MoldDetailView
class MoldDetailView(LoginRequiredMixin,DetailView):
    model = Mold
    template_name = 'mold/mold_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"suppliers","menu3":"suppliers","menu4":"mold","menu5":"detail"}
        context['supplier'] = Supplier.objects.get(pk=self.kwargs['pk'])
        return context

 ## 10.3 CreateMoldView
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

 ## 10.4 ProductPriceUpdateView
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

 ## 10.5 MoldDeleteView
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
