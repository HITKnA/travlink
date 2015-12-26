# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0013_auto_20151225_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='Image',
            field=models.ImageField(upload_to=b'./upload/headimage/', blank=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='Image',
            field=models.ImageField(null=True, upload_to=b'./diary/', blank=True),
        ),
    ]
