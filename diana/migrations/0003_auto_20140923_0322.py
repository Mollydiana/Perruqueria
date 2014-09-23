# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diana', '0002_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
