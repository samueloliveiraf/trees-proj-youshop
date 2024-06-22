from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, User


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email',)

    def save(self, commit=True):
        account = super(AccountCreationForm, self).save(commit=False)
        account.is_staff = True
        account.is_superuser = True
        if commit:
            account.save()
        return account


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('account',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.filter(is_superuser=True)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        account_email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        account = Account.objects.create_user(email=account_email, password=password)
        user.user = account
        if commit:
            user.save()
        return user
