from django.contrib import admin
from django import forms
from .models import Artiles
from ckeditor.widgets import CKEditorWidget


admin.site.register(Artiles)

class ArtilesAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())
    fill_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Artiles
        fields = ['title', 'id']
        list_display = ('title', 'id')

class ArtilesAdmin(admin.ModelAdmin):
    form = ArtilesAdminForm
