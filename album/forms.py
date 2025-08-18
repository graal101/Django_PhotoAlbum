# Добавлено при подк. загрузки картинок
from django import forms

from .models import UplPict


class UplPictForm(forms.ModelForm):
    class Meta:
        model = UplPict
        fields = ['name', 'UpPict_Img']
