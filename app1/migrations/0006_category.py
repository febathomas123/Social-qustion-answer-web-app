# Generated by Django 4.1.1 on 2022-10-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_p_reg_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
