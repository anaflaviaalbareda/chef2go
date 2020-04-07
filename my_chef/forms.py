from django import forms
from django.db import models
from django.forms import formset_factory, modelformset_factory

#Crispy forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class Contacto(forms.Form):

	Nombre= forms.CharField(label=False,widget=forms.TextInput(
		attrs={
			'class':'form-control', 'placeholder':'Nombre',
		}),required=True)
	Telefono= forms.CharField(label=False,widget=forms.TextInput(
		attrs={
			'class':'form-control','placeholder':'Telefono'
		}),required=True)
	Email=forms.EmailField(label=False,widget= forms.EmailInput(
		attrs={'class':'form-control','placeholder':'Email',
		}),required=True)
	Mensaje = forms.CharField(label=False,widget=forms.Textarea(
		attrs={
			'class':'form-control', 'placeholder':'Mensaje',
			}),required=True)


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout = Layout(
            Row(
                Column('Nombre', css_class='form-group col-md-4 mb-0'),
                Column('Telefono', css_class='form-group col-md-4 mb-0'),
                Column('Email', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
            	Column('Mensaje', css_class='form-group col'),
            	css_class='form-row'
            ),
        )
