# Generated by Django 3.0.3 on 2020-02-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshopa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petshop',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
