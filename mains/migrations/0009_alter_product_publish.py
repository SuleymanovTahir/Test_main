# Generated by Django 5.0.1 on 2024-01-29 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0008_alter_product_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 29, 22, 21, 14, 433132, tzinfo=datetime.timezone.utc)),
        ),
    ]