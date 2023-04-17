from django.forms import ModelForm, EmailInput
from Proveedor.models import Proveedor

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor;
        fields = '__all__';
        widgets = {
            'email': EmailInput(attrs={'type': 'email',
            'class': "form-control",
            'style': 'max-width 100px;',
            'placeholder':'Correo' }),
        };