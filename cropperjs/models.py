# coding=utf-8

from django.db import models

from .widgets import CropperWidget
from .fields import CropperImageFormField


class CropperImageField(models.ImageField):

    description = "A field derived from ImageField that automatically provides CropperJS functionality on client-side."

    __extra_arguments = [
        # float, optional: "suggests" (as in, can be overriden at client-side) a fixed proportion for the Cropper component
        'aspectratio',

        # tuple(int, int), optional: sets fixed dimensions for the image.
        # If provided, will automatically calculate the appropriate aspectratio
        'dimensions',

        # bool, optional: linked Cropper fields are called consecutively after calling any other in the same
        # context (those outside inlines, inline groups), using the same image provided by the user
        'linked'
    ]

    def __init__(self, verbose_name=None, name=None, dimensions=None, aspectratio=None, linked=False, **kwargs):
        self.dimensions, self.aspectratio, self.linked = dimensions, aspectratio, linked
        if self.dimensions:
            self.aspectratio = str(float(self.dimensions[0]) / float(self.dimensions[1])).replace(",", ".")

        super(CropperImageField, self).__init__(verbose_name, name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CropperImageField, self).deconstruct()

        for argname in self.__extra_arguments:
            value = getattr(self, argname, None)
            if value:
                kwargs[argname] = value

        return name, path, args, kwargs

    def formfield(self, **kwargs):
        kwargs.update({
            'form_class': CropperImageFormField,
            'widget': CropperWidget,
        })
        for field in self.__extra_arguments:
            kwargs.update({ field: getattr(self, field, None) })

        return super(CropperImageField, self).formfield(**kwargs)

