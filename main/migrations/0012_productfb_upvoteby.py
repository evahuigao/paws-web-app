# Generated by Django 4.0.3 on 2022-04-11 03:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_productfb_date_sellerfb_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfb',
            name='upvoteby',
            field=models.ManyToManyField(related_name='upvoter', to=settings.AUTH_USER_MODEL),
        ),
    ]
