from django import forms
from django.utils.timezone import make_aware
from .models import Capsule
from zoneinfo import ZoneInfo

class CapsuleForm(forms.ModelForm):
    unlock_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Capsule
        fields = ['title', 'message', 'unlock_date', 'image', 'video', 'audio']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)  # capture request
        super().__init__(*args, **kwargs)

    def clean_unlock_date(self):
        unlock_date = self.cleaned_data['unlock_date']

        tz_name = None
        if self.request:
            tz_name = self.request.POST.get("timezone")

        if tz_name:
            local_tz = ZoneInfo(tz_name)
            unlock_date = unlock_date.replace(tzinfo=local_tz)
            unlock_date = unlock_date.astimezone(ZoneInfo("UTC"))  # store in UTC
        else:
            unlock_date = make_aware(unlock_date)

        return unlock_date
