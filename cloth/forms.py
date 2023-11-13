from django import forms
from .models import OrderCL

class OrderForm(forms.ModelForm):
    customer_name = forms.CharField(max_length=50)
    class Meta:
        model = OrderCL
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

