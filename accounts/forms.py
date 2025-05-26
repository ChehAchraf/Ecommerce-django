from django import forms
from .models import Account
class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password  = forms.CharField(widget=forms.PasswordInput())
    
    
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','email','phone','country']
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password : 
            raise forms.ValidationError("Your password didn't mutch! ")
        return cleaned_data