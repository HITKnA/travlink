# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0014_auto_20151226_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='Image',
            field=models.ImageField(upload_to=b'./headimage/', blank=True),
        ),
    ]
