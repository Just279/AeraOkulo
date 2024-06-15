from django.forms import ModelForm

from .models import Vidbendo, Foto, Arkivo

class ModelVidbendo(ModelForm):
    class Meta:
        model=Vidbendo
        fields=(
            'upload',
                )

class ModelFoto(ModelForm):
    class Meta:
        model=Foto
        fields=(
            'upload',
                )

class ModelArkivo(ModelForm):
    class Meta:
        model=Arkivo
        fields=(
            'upload',
                )
