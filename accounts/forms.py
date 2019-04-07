from django import forms
from django.contrib.auth import authenticate
from .models import CreateUser


class SignUpForm(forms.ModelForm):
    Provider = 'P'
    Seeker   = 'S'
    CHOICES = ((Provider, 'Provider'), (Seeker, 'Seeker'))      
    FirstName    = forms.CharField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'FirstName...'}))
    LastName     = forms.CharField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'LastName...'}))
    Email        = forms.EmailField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'Email...'}))
    Password     = forms.CharField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'Password...'}))
    Country      = forms.CharField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'Country...'}))
    State        = forms.CharField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'State...'}))
    City         = forms.CharField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'City...'}))
    Company      = forms.CharField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'Company...'}))
    Acc_Type     = forms.CharField(widget=forms.Select(choices=CHOICES))


    class Meta:
        model = CreateUser
        fields = ('username','FirstName' , 'LastName', 'Email', 'Password' , 'Country' , 'State', 'City', 'Company' , 'Acc_Type')
    def clean(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError("username with this name is found, change it")
        except User.DoesNotExist:
            pass
    # def clean(self):
    #     if self.cleaned_data['Email'] and CreateUser.objects.filter(Email=self.cleaned_data['Email']).exists():
    #         raise forms.ValidationError("Email addresses must be unique")
    #     return super(SignUpForm, self).clean()

class LoginForm(forms.ModelForm):
    Email        = forms.EmailField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'Email...'}))
    Password     = forms.CharField(widget=forms.TextInput(attrs={'class': 'effect-2' , 'placeholder':'Password...'}))
    def clean(self , *args, **kwargs):
        Email    = self.cleaned_data['Email']
        Password = self.cleaned_data['Pass']
        user_qs  = CreateUser.objects.filter(Email = Email)
        user     = user_qs.first()
        if Email and Password:
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(Password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")

        return super(LoginForm, self).clean(*args, **kwargs)


