# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Test, TestImage


class TestImageInline(admin.TabularInline):
    model = TestImage
    extra = 1

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    fields = (
        ('title', 'image',),
        'image2'
    )
    inlines = [TestImageInline]
