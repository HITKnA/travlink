# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0010_diary_abstract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=20, null=True, blank=True)),
                ('Member', models.ManyToManyField(to='share.Account')),
                ('Travel_plan', models.ForeignKey(to='share.Travel_plan')),
            ],
        ),
    ]
