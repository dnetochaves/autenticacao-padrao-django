from ..models import Usuario
from django import forms


class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label="senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação senha", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ("email", "nome")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas informadas não são iguais")
        return password2
