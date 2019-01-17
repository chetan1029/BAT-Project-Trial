from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from settings.models import (Category, Status, Currency, Color, Size,
                             AmazonMarket, Box)
from settings.forms import (CategoryForm, StatusForm, CurrencyForm, ColorForm, SizeForm,
                            AmazonMarketForm, BoxForm)
from django.db.models import Q
# Create your views here.
# 1. Basic
 ## 1.1 Category
  ### 1.1.1 CategoryListView
  ### 1.1.2 CreateCategoryView
  ### 1.1.3 CategoryUpdateView
  ### 1.1.4 CategoryDeleteView
 ## 1.2 Color
  ### 1.2.1 ColorListView
  ### 1.2.2 CreateColorView
  ### 1.2.3 ColorUpdateView
  ### 1.2.4 ColorDeleteView
 ## 1.3 Size
  ### 1.3.1 SizeListView
  ### 1.3.2 CreateSizeView
  ### 1.3.3 SizeUpdateView
  ### 1.3.4 SizeDeleteView
 ## 1.4 Status
  ### 1.4.1 StatusListView
  ### 1.4.2 CreateStatusView
  ### 1.4.3 StatusUpdateView
  ### 1.4.4 StatusDeleteView
 ## 1.5 Currecy
  ### 1.5.1 CurrecyListView
  ### 1.5.2 CreateCurrecyView
  ### 1.5.3 CurrecyUpdateView
  ### 1.5.4 CurrecyDeleteView
 ## 1.5 Box
  ### 1.5.1 BoxListView
  ### 1.5.2 CreateBoxView
  ### 1.5.3 BoxUpdateView
  ### 1.5.4 BoxDeleteView

# 2. Amazon
 ## 2.1 AmazonMarket
  ### 2.1.1 AmazonMarketListView
  ### 2.1.2 CreateAmazonMarketView
  ### 2.1.3 AmazonMarketUpdateView
  ### 2.1.4 AmazonMarketDeleteView

# 1. Basic
 ## 1.1 Category
  ### 1.1.1 CategoryListView
class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'category/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"category"}
        return context

  ### 1.1.2 CreateCategoryView
class CreateCategoryView(LoginRequiredMixin,CreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'category/category_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"category"}
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
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"category"}
        return context

  ### 1.1.4 CategoryDeleteView
class CategoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('settings:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"category"}
        return context

 ## 1.2 Color
  ### 1.2.1 ColorListView
class ColorListView(LoginRequiredMixin,ListView):
    model = Color
    template_name = 'color/color_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"color"}
        return context

  ### 1.2.2 CreateColorView
class CreateColorView(LoginRequiredMixin,CreateView):
    form_class = ColorForm
    model = Color
    template_name = 'color/color_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"color"}
        return context

  ### 1.2.3 ColorUpdateView
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
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"color"}
        return context

  ### 1.2.4 ColorDeleteView
class ColorDeleteView(LoginRequiredMixin,DeleteView):
    model = Color
    template_name = 'color/color_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('settings:color_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"color"}
        return context

 ## 1.3 Size
  ### 1.3.1 SizeListView
class SizeListView(LoginRequiredMixin,ListView):
    model = Size
    template_name = 'size/size_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"size"}
        return context

  ### 1.3.2 CreateSizeView
class CreateSizeView(LoginRequiredMixin,CreateView):
    form_class = SizeForm
    model = Size
    template_name = 'size/size_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"size"}
        return context

  ### 1.3.3 SizeUpdateView
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
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"size"}
        return context

  ### 1.3.4 SizeDeleteView
class SizeDeleteView(LoginRequiredMixin,DeleteView):
    model = Size
    template_name = 'size/size_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('settings:size_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"size"}
        return context

 ## 1.4 Status
  ### 1.4.1 StatusListView
class StatusListView(LoginRequiredMixin,ListView):
    model = Status
    template_name = 'status/status_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"status"}
        return context

  ### 1.4.2 CreateStatusView
class CreateStatusView(LoginRequiredMixin,CreateView):
    form_class = StatusForm
    model = Status
    template_name = 'status/status_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"status"}
        return context

  ### 1.4.3 StatusUpdateView
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
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"status"}
        return context

  ### 1.4.4 StatusDeleteView
class StatusDeleteView(LoginRequiredMixin,DeleteView):
    model = Status
    template_name = 'status/status_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('settings:status_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"status"}
        return context

 ## 1.5 Currency
  ### 1.5.1 CurrencyListView
class CurrencyListView(LoginRequiredMixin,ListView):
    model = Currency
    template_name = 'currency/currency_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"currency"}
        return context

  ### 1.5.2 CreateCurrencyView
class CreateCurrencyView(LoginRequiredMixin,CreateView):
    form_class = CurrencyForm
    model = Currency
    template_name = 'currency/currency_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"currency"}
        return context

  ### 1.5.3 CurrencyUpdateView
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
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"currency"}
        return context

  ### 1.5.4 CurrencyDeleteView
class CurrencyDeleteView(LoginRequiredMixin,DeleteView):
    model = Currency
    template_name = 'currency/currency_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('settings:currency_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"currency"}
        return context

 ## 1.5 Box
  ### 1.5.1 BoxListView
class BoxListView(LoginRequiredMixin,ListView):
    model = Box
    template_name = 'box/box_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"box"}
        return context

  ### 1.5.2 CreateBoxView
class CreateBoxView(LoginRequiredMixin,CreateView):
    form_class = BoxForm
    model = Box
    template_name = 'box/box_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"box"}
        return context

  ### 1.5.3 BoxUpdateView
class BoxUpdateView(LoginRequiredMixin,UpdateView):
    form_class = BoxForm
    model = Box
    template_name = 'box/box_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"box"}
        return context

  ### 1.5.4 BoxDeleteView
class BoxDeleteView(LoginRequiredMixin,DeleteView):
    model = Box
    template_name = 'box/box_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('settings:box_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"basic","menu4":"box"}
        return context

# 2. Amazon
 ## 2.1 AmazonMarket
  ### 2.1.1 AmazonMarketListView
class AmazonMarketListView(LoginRequiredMixin,ListView):
    model = AmazonMarket
    template_name = 'amazonmarket/amazonmarket_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"amazon","menu4":"market"}
        return context

  ### 2.1.2 CreateAmazonMarketView
class CreateAmazonMarketView(LoginRequiredMixin,CreateView):
    form_class = AmazonMarketForm
    model = AmazonMarket
    template_name = 'amazonmarket/amazonmarket_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"amazon","menu4":"market"}
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
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"amazon","menu4":"market"}
        return context

  ### 2.1.4 AmazonMarketDeleteView
class AmazonMarketDeleteView(LoginRequiredMixin,DeleteView):
    model = AmazonMarket
    template_name = 'amazonmarket/amazonmarket_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('settings:amazonmarket_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu'] = {"menu1":"basic","menu2":"settings","menu3":"amazon","menu4":"market"}
        return context
