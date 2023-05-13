from django import forms
import re
from event.models import Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

    def clean_rg(self):
        rg = self.cleaned_data['rg']
        if Enrollment.objects.filter(rg=rg).exists():
            raise forms.ValidationError('RG já registrado')
        return rg
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Enrollment.objects.filter(email=email).exists():
            raise forms.ValidationError('EMAIL já existente')
        return email
