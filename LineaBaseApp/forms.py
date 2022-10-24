from django.db.models import fields
from django.forms import ModelForm, forms
from .models import tb_usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UsuarioForm(ModelForm):
    class Meta:
        model = tb_usuario
        fields = '__all__'
        
class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']