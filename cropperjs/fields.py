# coding=utf-8

from django import forms
from .widgets import CropperWidget
from .utils import cropperImageFile, TEXT_TYPE

class CropperImageFormField(forms.ImageField):
    widget = CropperWidget

    def __init__(self, aspectratio=None, dimensions=None, linked=None, **kwargs):
        self.aspectratio, self.dimensions, self.linked = aspectratio, dimensions, linked
        super(CropperImageFormField, self).__init__(**kwargs)


    def widget_attrs(self, widget):
        attrs = super(CropperImageFormField, self).widget_attrs(widget)
        attrs.update({
            'label': self.label,
            'aspectratio': str(self.aspectratio).replace(",", ".") if self.aspectratio else "",
            'dimensions': self.dimensions,
            'linked': self.linked,
        })
        return attrs


    def clean(self, data, initial=None):

        if self.has_changed(initial, data):

            if data is None or len(data) == 0:
                if self.required:
                    raise forms.ValidationError(self.error_messages['required'])
                else:
                    return ""

            else:
                try:
                    contentFile = cropperImageFile(data, "image")
                    return contentFile
                except ValueError:
                    raise forms.ValidationError(self.default_error_messages['invalid_image'])

        else: # Unchanged
            return initial


    def has_changed(self, initial, data):
        if not data:
            # If data is empty and initial exists, field has changed
            return initial != None
        else:
            if isinstance(data, TEXT_TYPE) and data[0] == "/":
                # If data is an url, field has changed if url is different than the initial value's url
                return str(initial.url) != str(data)
            else:
                # Otherwise, assumes it's a ContentFile and therefore field has changed
                return True
