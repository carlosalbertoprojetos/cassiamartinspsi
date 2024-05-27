from django import forms
from django.utils.safestring import mark_safe

class CKEditor5Widget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        self.config_name = kwargs.pop('config_name', 'default')
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs, renderer)
        return mark_safe(rendered + f'<script src="/static/ckeditor5/build/ckeditor.js"></script>'
                                   f'<script>ClassicEditor.create(document.querySelector(\'[name="{name}"]\'));</script>')
