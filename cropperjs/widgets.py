# coding=utf-8

from django.forms.widgets import ClearableFileInput
from .utils import TEXT_TYPE

class CropperWidget(ClearableFileInput):
    template_name = "cropperjs/widgets/cropperjs.html"

    def value_from_datadict(self, data, files, name):
        filedata = data[name]
        return filedata if filedata and filedata != "" else None

    def format_value(self, value):
        # Value will be either the URL/base64 string from an unchanged field,
        # or the initial ImageFieldFile object
        if isinstance(value, TEXT_TYPE):
            return value
        elif value:
            return value.url
        return None

    class Media:
        js = ("js/cropper.min.js", "js/cropper.extra.js")
        css = {'all': ("css/cropper.min.css", "css/cropper.extra.css")}
