# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0012_auto_20151221_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='Image',
            field=models.ImageField(upload_to=b'./headimage/', blank=True),
        ),
    ]
