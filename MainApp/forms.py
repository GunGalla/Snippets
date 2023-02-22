from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput
from MainApp.models import Snippet, Comment
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['name', 'lang', 'code']
        labels = {'name': '', 'lang': '', 'code': ''}
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Назание сниппета'}),
            'code': Textarea(attrs={'placeholder': 'Код сниппета'}),
        }


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    password1 = CharField(label="password", widget=PasswordInput)
    password2 = CharField(label="password confirm", widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) >=5 and username[0].isupper():
            return username
        else:
            return ValidationError(
                'Имя должно быть больше 5 символов и первй символ в верхнем регистре.'
            )

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise ValidationError("Пароли не совпадают или пустые")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CommentForm(ModelForm):
   class Meta:
       model = Comment
       fields = ["text", 'image']
       labels = {'text': ''}