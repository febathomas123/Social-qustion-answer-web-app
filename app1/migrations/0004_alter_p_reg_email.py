# Generated by Django 4.1.1 on 2022-09-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_p_reg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_reg',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]