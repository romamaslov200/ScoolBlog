from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import text_home

admin.site.register(text_home)

class text_homeAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())
    fill_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = text_home
        fields = '__all__'

class text_homeAdmin(admin.ModelAdmin):
    form = text_homeAdminForm
