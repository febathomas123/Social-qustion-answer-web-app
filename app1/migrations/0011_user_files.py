# Generated by Django 4.1.1 on 2022-10-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_expert_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='files',
            field=models.FileField(null=True, upload_to='proof/%m'),
        ),
    ]
