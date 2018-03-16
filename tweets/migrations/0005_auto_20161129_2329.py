# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140, validators=[tweets.models.validate_content]),
        ),
    ]
