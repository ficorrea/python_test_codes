from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from gas.core.util import generate_hash_key
# from .models import PasswordReset

User = get_user_model()


class PasswordResetForm(forms.Form):

    username = forms.CharField(label='Login')

    def clean_login(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            return username
        raise forms.ValidationError('Nenhum usuário encontrado com este login')

    def save(self):
        user = User.objects.get(username=self.cleaned_data['username'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'login.html'
        subject = 'Criar nova senha no Mortugas'
        context = {'reset': reset, }


class RegisterForm(forms.ModelForm):

    username = forms.EmailField(label='Login')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'A confirmação não está correta', code='password_mismatch')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']


class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name']
