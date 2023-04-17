from django.forms import ModelForm, DateInput, Textarea
from Comentario.models import Comentario

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__';
        widgets = {
            'contenido':Textarea(attrs={'rows': 3}),
            'fecha_publicacion': DateInput(attrs={'type': 'date'})
        };
