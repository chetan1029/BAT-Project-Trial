from django import forms
from shipping.models import (Shipment)

# form details
# 1. ShipmentForm
 ## 1.1 ShipmentForm

# 1. ShipmentForm
 ## 1.1 ShipmentForm
class ShipmentForm(forms.ModelForm):

    class Meta:
        model = Shipment
        fields = ('name','order','packing_type','type','kg_cbm_price','currency','invoice_agent','invoice_value','invoice_currency','carrier','prepaid_vat','vat_currency','actual_vat','vat_claimed','pickup_date','eta','etd','tracking_id','status')
