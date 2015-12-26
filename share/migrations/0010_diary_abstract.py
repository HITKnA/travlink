# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0009_auto_20151121_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='Abstract',
            field=models.TextField(null=True, blank=True),
        ),
    ]
