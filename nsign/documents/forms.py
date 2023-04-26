from django import forms

from nsign.documents.models import Document


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"aria-label": "", "class": "col", "placeholder": "Введите имя документа"}),
            "description": forms.Textarea(attrs={"aria-label": "", "class": "col", "placeholder": "Введите содержание документа"}),
        }


class DocumentUpdateForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ["id", "name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"aria-label": "", "class": "col col-2", "placeholder": "Введите имя документа"}),
            "description": forms.Textarea(attrs={"aria-label": "", "class": "col col-3", "placeholder": "Введите содержание документа"}),
        }
