# Generated by Django 4.1.1 on 2022-09-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='E_reg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
