from django import forms
from ckeditor.widgets import CKEditorWidget
from django_json_widget.widgets import JSONEditorWidget
from .models import Home


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ("titulo", "foto", "letreiro", "redes_sociais", "atual")
        widgets = {
            "letreiro": JSONEditorWidget(options={"mode": "tree"}),
            "texto": CKEditorWidget(),  # Adicionando o CKEditor para o campo texto
        }
