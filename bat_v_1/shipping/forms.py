from django import forms
from shipping.models import (Shipment, ShipmentProduct)

# form details
# 1. ShipmentForm
 ## 1.1 ShipmentForm
 ## 1.2 ShipmentProductForm

# 1. ShipmentForm
 ## 1.1 ShipmentForm
class ShipmentForm(forms.ModelForm):

    class Meta:
        model = Shipment
        fields = ('name','order','packing_type','type','kg_cbm_price','currency','invoice_agent','invoice_value','invoice_currency','carrier','prepaid_vat','vat_currency','actual_vat','vat_claimed','pickup_date','eta','etd','tracking_id','status')
        widgets = {
            'pickup_date': forms.TextInput(attrs={'class': 'datepicker'}),
            'eta': forms.TextInput(attrs={'class': 'datepicker'}),
            'etd': forms.TextInput(attrs={'class': 'datepicker'})
        }

 ## 1.2 ShipmentProductForm
class ShipmentProductForm(forms.ModelForm):

    class Meta:
        model = ShipmentProduct
        fields = ('product','amazonproduct','quantity_send','quantity_received','missing_units')
