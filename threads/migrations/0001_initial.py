# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-09-04 11:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', tinymce.models.HTMLField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'SOME STRING', max_length=255)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'SOME STRING', max_length=255)),
                ('DOB', models.CharField(default=b'SOME STRING', max_length=255)),
                ('diagnosis', models.CharField(default=b'SOME STRING', max_length=255)),
                ('GMFCS', models.CharField(default=b'SOME STRING', max_length=255)),
                ('therapist', models.CharField(default=b'SOME STRING', max_length=255)),
                ('lying', models.CharField(default=b'SOME STRING', max_length=255)),
                ('sitting', models.CharField(default=b'SOME STRING', max_length=255)),
                ('standing', models.CharField(default=b'SOME STRING', max_length=255)),
                ('walking', models.CharField(default=b'SOME STRING', max_length=255)),
                ('Hipxray', models.CharField(default=b'SOME STRING', max_length=255)),
                ('NextHipxray', models.CharField(default=b'SOME STRING', max_length=255)),
                ('spineXray', models.CharField(default=b'SOME STRING', max_length=255)),
                ('NextspineXray', models.CharField(default=b'SOME STRING', max_length=255)),
                ('BTXA', models.CharField(default=b'SOME STRING', max_length=255)),
                ('baclofen', models.CharField(default=b'SOME STRING', max_length=255)),
                ('SDR', models.CharField(default=b'SOME STRING', max_length=255)),
                ('other', models.CharField(default=b'SOME STRING', max_length=255)),
                ('PreviousOrthopaedicManagement', models.CharField(default=b'SOME STRING', max_length=255)),
                ('OrthopaedicGoals', models.CharField(default=b'SOME STRING', max_length=255)),
                ('FunctionalGoals', models.CharField(default=b'SOME STRING', max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='threads.Subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='threads.Thread'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
