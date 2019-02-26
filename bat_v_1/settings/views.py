from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from settings.models import (Category, Status, Currency,
                             AmazonMarket, AmazonMwsauth)
from settings.forms import (CategoryForm, StatusForm, CurrencyForm,
                            AmazonMarketForm, AmazonMwsauthForm)
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models.deletion import ProtectedError
from django.contrib import messages
import logging
import requests
logger = logging.getLogger(__name__)
# Create your views here.
# 1. Basic
 ## 1.1 Category
  ### 1.1.1 CategoryListView
  ### 1.1.2 CreateCategoryView
  ### 1.1.3 CategoryUpdateView
  ### 1.1.4 CategoryDeleteView
 ## 1.2 Status
  ### 1.2.1 StatusListView
  ### 1.2.2 CreateStatusView
  ### 1.2.3 StatusUpdateView
  ### 1.2.4 StatusDeleteView
 ## 1.3 Currecy
  ### 1.3.1 CurrecyListView
  ### 1.3.2 CreateCurrecyView
  ### 1.3.3 CurrecyUpdateView
  ### 1.3.4 CurrecyDeleteView
 ## 1.4 Box
  ### 1.4.1 BoxListView
  ### 1.4.2 CreateBoxView
  ### 1.4.3 BoxUpdateView
  ### 1.4.4 BoxDeleteView

# 2. Amazon
 ## 2.1 AmazonMarket
  ### 2.1.1 AmazonMarketListView
  ### 2.1.2 CreateAmazonMarketView
  ### 2.1.3 AmazonMarketUpdateView
  ### 2.1.4 AmazonMarketDeleteView
 ## 2.2 AmazonMwsauth
  ### 2.2.1 AmazonMwsauthListView
  ### 2.2.2 CreateAmazonMwsauthView
  ### 2.2.3 AmazonMwsauthUpdateView
  ### 2.2.4 AmazonMwsauthDeleteView


# 1. Basic
 ## 1.1 Category
  ### 1.1.1 CategoryListView
class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'category/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"category","menu3":"basic","menu4":"category"}
        return context

  ### 1.1.2 CreateCategoryView
class CreateCategoryView(LoginRequiredMixin,CreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'category/category_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"category","menu3":"basic","menu4":"category"}
        return context

  ### 1.1.3 CategoryUpdateView
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
        context['active_menu'] = {"menu1":"setting","menu2":"category","menu3":"basic","menu4":"category"}
        return context

  ### 1.1.4 CategoryDeleteView
class CategoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_message = "%(name)s was deleted successfully"
    protected_error = "can't delete %(name)s because it is used by other forms"

    def get_success_url(self):
        return reverse_lazy('settings:category_list')

    def get_error_url(self):
        return reverse_lazy('settings:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"category","menu3":"basic","menu4":"category"}
        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        get_success_url = self.get_success_url()
        get_error_url = self.get_error_url()
        try:
            obj.delete()
            messages.success(self.request, self.success_message % obj.__dict__)
            return HttpResponseRedirect(get_success_url)
        except ProtectedError:
            messages.warning(self.request, self.protected_error % obj.__dict__)
            return HttpResponseRedirect(get_error_url)

  ### 1.1.5 View Functions for Categories
def load_display_categories(request):
    category_id = request.GET.get('category')
    active = request.GET.get('active')
    if active:
        active = int(active)

    if category_id:
        parent_category_id = Category.objects.get(pk=category_id).parent_id
        subcategory = Category.objects.filter(parent=category_id)
        category_breadcrumbs = Category.objects.get(pk=category_id).category_breadcrumbs
    else:
        parent_category_id = "parent"
        subcategory = Category.objects.filter(parent__isnull=True)
        category_breadcrumbs = ""

    return render(request, 'category/ajax/category_display.html',{'categories':subcategory,'category_id':category_id,'parent_category_id':parent_category_id,'active':active, 'category_breadcrumbs':category_breadcrumbs})

def add_category(request):
    parent_id = request.POST.get('parent_id')
    name = request.POST.get('name')
    category_id = request.POST.get('category_id')

    if category_id:
        category = Category.objects.get(pk=category_id)
        category.name = name
        category.save()
    else:
        if parent_id:
            cat_parent = Category.objects.get(pk=parent_id)
            category = Category.objects.create(name=name,parent=cat_parent)
        else:
            category = Category.objects.create(name=name)

    data = {
        'parent_id':parent_id,
        'name': name,
        'success': True
    }
    return JsonResponse(data)

 ## 1.2 Status
  ### 1.2.1 StatusListView
class StatusListView(LoginRequiredMixin,ListView):
    model = Status
    template_name = 'status/status_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"status","menu3":"basic","menu4":"status"}
        return context

  ### 1.2.2 CreateStatusView
class CreateStatusView(LoginRequiredMixin,CreateView):
    form_class = StatusForm
    model = Status
    template_name = 'status/status_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"status","menu3":"basic","menu4":"status"}
        return context

  ### 1.2.3 StatusUpdateView
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
        context['active_menu'] = {"menu1":"setting","menu2":"status","menu3":"basic","menu4":"status"}
        return context

  ### 1.2.4 StatusDeleteView
class StatusDeleteView(LoginRequiredMixin,DeleteView):
    model = Status
    template_name = 'status/status_confirm_delete.html'
    success_message = "%(title)s was deleted successfully"
    protected_error = "can't delete %(title)s because it is used by other forms"

    def get_success_url(self):
        return reverse_lazy('settings:status_list')

    def get_error_url(self):
        return reverse_lazy('settings:status_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"status","menu3":"basic","menu4":"status"}
        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        get_success_url = self.get_success_url()
        get_error_url = self.get_error_url()
        try:
            obj.delete()
            messages.success(self.request, self.success_message % obj.__dict__)
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(self.request, self.protected_error % obj.__dict__)
            return HttpResponseRedirect(get_error_url)

  ### 1.2.5 View Functions for Status
def load_display_status(request):
    status_id = request.GET.get('status')
    active = request.GET.get('active')
    if active:
        active = int(active)

    if status_id:
        parent_status_id = Status.objects.get(pk=status_id).parent_id
        substatus = Status.objects.filter(parent=status_id)
        status_breadcrumbs = Status.objects.get(pk=status_id).status_breadcrumbs
    else:
        parent_status_id = "parent"
        substatus = Status.objects.filter(parent__isnull=True)
        status_breadcrumbs = ""

    return render(request, 'status/ajax/status_display.html',{'statuses':substatus,'status_id':status_id,'parent_status_id':parent_status_id,'active':active, 'status_breadcrumbs':status_breadcrumbs})

def add_status(request):
    parent_id = request.POST.get('parent_id')
    title = request.POST.get('name')
    status_id = request.POST.get('status_id')

    if status_id:
        status = Status.objects.get(pk=status_id)
        status.title = title
        status.save()
    else:
        if parent_id:
            status_parent = Status.objects.get(pk=parent_id)
            status = Status.objects.create(title=title,parent=status_parent)
        else:
            status = Status.objects.create(title=title)

    data = {
        'parent_id':parent_id,
        'title': title,
        'success': True
    }
    return JsonResponse(data)

 ## 1.3 Currency
  ### 1.3.1 CurrencyListView
class CurrencyListView(LoginRequiredMixin,ListView):
    model = Currency
    template_name = 'currency/currency_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"catalog","menu3":"basic","menu4":"currency"}
        return context

  ### 1.3.2 CreateCurrencyView
class CreateCurrencyView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = CurrencyForm
    model = Currency
    success_message = "%(title)s was created successfully"
    template_name = 'currency/currency_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"catalog","menu3":"basic","menu4":"currency"}
        return context

  ### 1.3.3 CurrencyUpdateView
class CurrencyUpdateView(SuccessMessageMixin, LoginRequiredMixin,UpdateView):
    form_class = CurrencyForm
    model = Currency
    template_name = 'currency/currency_form.html'
    success_message = "%(title)s was updated successfully"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"catalog","menu3":"basic","menu4":"currency"}
        return context


  ### 1.3.4 CurrencyDeleteView
class CurrencyDeleteView(LoginRequiredMixin,DeleteView):
    model = Currency
    template_name = 'currency/currency_confirm_delete.html'
    success_message = "%(title)s was deleted successfully"
    protected_error = "can't delete %(title)s because it is used by other forms"

    def get_success_url(self):
        return reverse_lazy('settings:currency_list')

    def get_error_url(self):
        return reverse_lazy('settings:currency_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"setting","menu2":"catalog","menu3":"basic","menu4":"currency"}
        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        get_success_url = self.get_success_url()
        get_error_url = self.get_error_url()
        try:
            obj.delete()
            messages.success(self.request, self.success_message % obj.__dict__)
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(self.request, self.protected_error % obj.__dict__)
            return HttpResponseRedirect(get_error_url)


 
# 2. Amazon
 ## 2.1 AmazonMarket
  ### 2.1.1 AmazonMarketListView
class AmazonMarketListView(LoginRequiredMixin,ListView):
    model = AmazonMarket
    template_name = 'amazonmarket/amazonmarket_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"sales-channels","menu2":"market"}
        return context

  ### 2.1.2 CreateAmazonMarketView
class CreateAmazonMarketView(LoginRequiredMixin,CreateView):
    form_class = AmazonMarketForm
    model = AmazonMarket
    template_name = 'amazonmarket/amazonmarket_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"sales-channels","menu2":"market"}
        return context

  ### 2.1.3 AmazonMarketUpdateView
class AmazonMarketUpdateView(LoginRequiredMixin,UpdateView):
    form_class = AmazonMarketForm
    model = AmazonMarket
    template_name = 'amazonmarket/amazonmarket_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"sales-channels","menu2":"market"}
        return context

  ### 2.1.4 AmazonMarketDeleteView
class AmazonMarketDeleteView(LoginRequiredMixin,DeleteView):
    model = AmazonMarket
    template_name = 'amazonmarket/amazonmarket_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('settings:amazonmarket_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"sales-channels","menu2":"market"}
        return context

def sync_amazonmarket(request,pk):
    amazonmarket = AmazonMarket.objects.get(pk=pk)

    amazonmwsauth = AmazonMwsauth.objects.get(region=amazonmarket.region)
    amazon_auth = {}
    amazon_auth["MarketPlaceId"] = amazonmarket.marketplace_id
    amazon_auth["SellerId"] = amazonmwsauth.seller_id
    amazon_auth["MWSAuthToken"] = amazonmwsauth.auth_token
    amazon_auth["AccessKey"] = amazonmwsauth.access_key
    amazon_auth["SecretKey"] = amazonmwsauth.secret_key

    sync_amazon_data = {
        "domain": amazonmarket.amazon_id,
        "amazon_auth": amazon_auth
    }

    response = requests.post("http://174.138.71.123/amazon/shipments/api/sync-amazonmarket.php", json=sync_amazon_data)
    response_data = response.json()
    logger.warning(response_data)

    return redirect('settings:amazonmarket_list')

 ## 2.2 AmazonMwsauth
  ### 2.2.1 AmazonMwsauthListView
class AmazonMwsauthListView(LoginRequiredMixin,ListView):
    model = AmazonMwsauth
    template_name = 'amazonmwsauth/amazonmwsauth_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"sales-channels","menu2":"mwsauth"}
        return context

  ### 2.1.2 CreateAmazonMarketView
class CreateAmazonMwsauthView(LoginRequiredMixin,CreateView):
    form_class = AmazonMwsauthForm
    model = AmazonMwsauth
    template_name = 'amazonmwsauth/amazonmwsauth_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"sales-channels","menu2":"mwsauth"}
        return context

  ### 2.1.3 AmazonMwsauthUpdateView
class AmazonMwsauthUpdateView(LoginRequiredMixin,UpdateView):
    form_class = AmazonMwsauthForm
    model = AmazonMwsauth
    template_name = 'amazonmwsauth/amazonmwsauth_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"sales-channels","menu2":"mwsauth"}
        return context

  ### 2.1.4 AmazonMwsauthDeleteView
class AmazonMwsauthDeleteView(LoginRequiredMixin,DeleteView):
    model = AmazonMwsauth
    template_name = 'amazonmwsauth/amazonmwsauth_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('settings:amazonmarket_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"sales-channels","menu2":"mwsauth"}
        return context
