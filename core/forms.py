from django import forms
from .utils import leap_year


class LeapYearForm(forms.Form):
    year = forms.CharField(label='Ano')

    def clean_year(self):
        year = self.cleaned_data['year']
        try:
            year = int(year)
        except ValueError:
            raise forms.ValidationError('Informe um ano válido')
        return year

    def is_leapyear(self):
        return leap_year(int(self.cleaned_data['year']))
