# Generated by Django 4.1.1 on 2022-10-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_expert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='cat',
            field=models.CharField(max_length=30),
        ),
    ]
