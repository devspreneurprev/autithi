from django import forms

from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)
User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        # return True
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'password1',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password != password1:
            raise forms.ValidationError("Password is not match")
        email = User.objects.filter(email=email)
        if email.exists():
            raise forms.ValidationError("This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
