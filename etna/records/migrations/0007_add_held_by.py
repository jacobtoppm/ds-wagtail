# Generated by Django 3.1.8 on 2021-07-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_auto_20210709_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordpage',
            name='held_by',
            field=models.TextField(blank=True),
        ),
    ]
