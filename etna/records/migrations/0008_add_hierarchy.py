# Generated by Django 3.1.8 on 2021-08-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_add_held_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordpage',
            name='hierarchy',
            field=models.JSONField(null=True),
        ),
    ]
