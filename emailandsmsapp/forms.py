from django import forms
from emailandsmsapp.models import RegModel
class RegForm(forms.ModelForm):
    class Meta:
        model=RegModel
        fields=['Fname','Lname','Uname','Password','Cpassword','Email','Mobno']
        widget={'password':forms.PasswordInput(),
                'Cpassword':forms.PasswordInput()}