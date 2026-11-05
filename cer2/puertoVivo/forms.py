from django import forms
from .models import LugarPatrimonial


class LugarPatrimonialForm(forms.ModelForm):

    class Meta:
        model = LugarPatrimonial

        fields = [
            'nombre',
            'descripcion',
            'ubicacion',
            'ano_construccion',
            'imagen',
            'categoria'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control'

        self.fields['categoria'].widget.attrs['class'] = 'form-select'
        self.fields['descripcion'].widget.attrs['rows'] = 4