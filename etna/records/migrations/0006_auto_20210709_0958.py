# Generated by Django 3.1.8 on 2021-07-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_alter_reference_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordpage',
            name='iaid',
            field=models.TextField(),
        ),
    ]
