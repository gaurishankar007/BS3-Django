from django import forms
from .models import *
from django.forms import ModelForm


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.IntegerField()


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'  # ["firstname", "lastname", "address"] to show only firstname and lastname


class FileForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'username']


class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = "__all__"


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"


