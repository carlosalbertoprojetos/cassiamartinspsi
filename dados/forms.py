from django import forms
from django_json_widget.widgets import JSONEditorWidget
from .models import Home


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = "__all__"
        widgets = {
            "letreiro": JSONEditorWidget(options={"mode": "tree"}),
        }
