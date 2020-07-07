from django import forms
from .models import Term

class SearchForm(forms.ModelForm):
	class Meta:
		model = Term
		fields = ('keyword',)
		widgets = {
			'keyword' : forms.TextInput(
				attrs = {
					'class' : 'form-control-sm'
				})
		}
