
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cropperjs.models import CropperImageField


class Test(models.Model):
    title = models.CharField("Título", max_length=255, blank=True, null=True)
    image = CropperImageField("Imagem de teste", linked=True, upload_to="image/")
    image2 = CropperImageField("Imagem de teste 2", dimensions=(400, 200), blank=True, null=True, upload_to="image2/")

    def __str__(self):
        return "%s / %s" % (self.image.name, self.image2.name)


class TestImage(models.Model):
    test = models.ForeignKey(Test)
    title = models.CharField("Title", max_length=255, blank=True, null=True)
    title2 = models.CharField("Title", max_length=255, blank=True, null=True)
    image = CropperImageField("Imagem inline #1", dimensions=(100, 100), linked=True, upload_to="1/")
    image2 = CropperImageField("Imagem inline #2", dimensions=(360, 100), linked=True, blank=True, null=True, upload_to="2/")
