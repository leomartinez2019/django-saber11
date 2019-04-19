from django import forms

class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control mr-sm-2'
            })

class ColegioForm(BootstrapForm):
    colegio = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'required': True, 'placeholder': 'Buscar'}))
    #ciudad = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required': True, 'placeholder': 'medellin'}))

    def clean(self):
        return dict((k, v.upper()) for k, v in self.cleaned_data.items())

class ColegioComparaForm(forms.Form):
    colegio1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'required': True, 'placeholder': 'ejemplo: montessori'}))
    ciudad1 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required': True, 'placeholder': 'medellin'}))
    colegio2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'required': True, 'placeholder': 'la salle'}))
    ciudad2 = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required': True, 'placeholder': 'barranquilla'}))
