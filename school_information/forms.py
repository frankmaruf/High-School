from django import forms
from school_information.models import NoticBoard
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingFormField


class Notic_Board_Form(forms.ModelForm):
    class Meta:
        model = NoticBoard
        fields = ("__all__")
        exclude = ['slug']