django-cropperjs
================

Adds `CropperJS`_\ ’s functionality to image fields in Django/Django CMS
admin, including inlines.

``CropperImageField`` is a subclass from ``ImageField``, and so can be
interchanged in your existing base without data loss.

Quick start
~~~~~~~~~~~

-  Add “cropperjs” to your INSTALLED_APPS setting like this:

::

       INSTALLED_APPS = [
           ...
           'cropperjs',
       ]

-  Change/set your model’s image field to use CropperImageField instead
   of ImageField.

::

       from cropperjs.models import CropperImageField

       image_field = CropperImageField(...)

Field options
~~~~~~~~~~~~~

All options from ``ImageField`` are (or should be) usable, like
``upload_to``. These below allow you to customize some of the CropperJS
component behavior on a field-to-field basis:

aspectratio: float


*Suggests* (as in, can be overriden later at client-side if needed) a
fixed proportion for the Cropper component, e.g. 1.7777 (16:9).

dimensions: tuple(int, int)


Defines a fixed dimension for the image generated. When informed,
calculates and overrides ``aspectratio``.

linked: bool


Linked Cropper fields are called consecutively after any other in the
same context (outside inlines, inline groups) is saved, using the same
original image specified by the user. Useful when the user needs the
same image but in different ways/sizes, e.g. a main image and a 1:1
thumbnail.

.. _CropperJS: https://fengyuanchen.github.io/cropperjs/
