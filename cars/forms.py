from django import forms
from cars.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'model': 'Modelo',
            'brand': 'Marca',
            'factory_year': 'Ano de fabricação',
            'model_year': 'Ano do modelo',
            'plate': 'Placa',
            'value': 'Valor',
            'photo': 'Foto',
            'bio': 'Descrição',
        }
        widgets = {
            'model': forms.TextInput(attrs={'placeholder': 'Ex: Civic'}),
            'factory_year': forms.NumberInput(attrs={'placeholder': 'Ex: 2010'}),
            'model_year': forms.NumberInput(attrs={'placeholder': 'Ex: 2011'}),
            'plate': forms.TextInput(attrs={'placeholder': 'Ex: ABC-1234'}),
            'value': forms.NumberInput(attrs={'placeholder': 'Ex: 35000.00'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Informações adicionais sobre o carro'}),
        }

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value', 'Valor mínimo do carro deve ser R$ 10.000,00')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1900:
            self.add_error('factory_year', 'O ano mínimo é 1900')
        return factory_year
