# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-17 18:33
from __future__ import unicode_literals

import cropperjs.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='T\xedtulo')),
                ('image', cropperjs.models.CropperImageField(linked=True, upload_to='image/', verbose_name='Imagem de teste')),
                ('image2', cropperjs.models.CropperImageField(aspectratio=b'2.0', blank=True, dimensions=(400, 200), null=True, upload_to='image2/', verbose_name='Imagem de teste 2')),
            ],
        ),
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('title2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('image', cropperjs.models.CropperImageField(aspectratio=b'1.0', dimensions=(100, 100), linked=True, upload_to='1/', verbose_name='Imagem inline #1')),
                ('image2', cropperjs.models.CropperImageField(aspectratio=b'3.6', blank=True, dimensions=(360, 100), linked=True, null=True, upload_to='2/', verbose_name='Imagem inline #2')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmodels.Test')),
            ],
        ),
    ]
