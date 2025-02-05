from django import forms
from shipping.models import (Shipment, ShipmentProduct, ShipmentProductOrderDelivery)

# form details
# 1. ShipmentForm
 ## 1.1 ShipmentForm
 ## 1.2 ShipmentProductForm

# 1. ShipmentForm
 ## 1.1 ShipmentForm
class ShipmentForm(forms.ModelForm):

    class Meta:
        model = Shipment
        fields = ('kg_cbm_price','currency','invoice_agent','invoice_value','invoice_currency','is_prepaid_vat','prepaid_vat','vat_currency','actual_vat','vat_claimed','pickup_date','eta','etd','bol_number')
        widgets = {
            'pickup_date': forms.TextInput(attrs={'class': 'datepicker'}),
            'eta': forms.TextInput(attrs={'class': 'datepicker'}),
            'etd': forms.TextInput(attrs={'class': 'datepicker'}),
            'invoice_value': forms.NumberInput(attrs={'min': '0'}),
            'prepaid_vat': forms.NumberInput(attrs={'min': '0'}),
            'actual_vat': forms.NumberInput(attrs={'min': '0'}),
            'kg_cbm_price': forms.NumberInput(attrs={'min': '0'})
        }

 ## 1.2 ShipmentProductForm
class ShipmentProductForm(forms.ModelForm):

    class Meta:
        model = ShipmentProduct
        fields = ('product','amazonproduct','quantity_send')

 ## 1.3 ShipmentProductForm
class ShipmentProductOrderDeliveryForm(forms.ModelForm):

    class Meta:
        model = ShipmentProductOrderDelivery
        fields = ('shipmentproduct','orderdelivery','quantity')
