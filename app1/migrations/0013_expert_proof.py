# Generated by Django 4.1.1 on 2022-10-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_remove_user_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='proof',
            field=models.FileField(null=True, upload_to='e_proof/%m'),
        ),
    ]
