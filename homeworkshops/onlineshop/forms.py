import datetime

from django import forms


class ProductFormWidget(forms.Form):
    title = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'product name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'product description'}))
    price = forms.FloatField(min_value=100, max_value=10_000,
                             widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01',
                                                             'placeholder': 'the cost of the product'}))
    amount = forms.IntegerField(min_value=0, max_value=100,
                                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'placeholder': 'in stock'}))
    date_added = forms.DateField(initial=datetime.date.today,
                                 widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date',
                                                               'placeholder': 'date the product was added'}))
    image = forms.ImageField(widget=forms.FileInput())
