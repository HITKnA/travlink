# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0011_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['-Date_time']},
        ),
        migrations.AddField(
            model_name='group',
            name='Date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
