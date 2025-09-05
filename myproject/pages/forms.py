from django import forms
from .models import FormModel

# -------- Way2 --------
class SimpleForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True
    )

# -------- Way3 --------
class ModelBasedForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }