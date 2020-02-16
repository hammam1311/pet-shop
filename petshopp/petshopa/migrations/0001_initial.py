# Generated by Django 3.0.3 on 2020-02-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('available', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]