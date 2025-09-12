from django import forms
from .models import Capsule

class CapsuleForm(forms.ModelForm):
    class Meta:
        model = Capsule
        fields = ['title', 'message', 'unlock_date', 'image', 'video', 'audio']
        widgets = {
            'unlock_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
        }
