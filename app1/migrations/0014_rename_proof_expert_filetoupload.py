# Generated by Django 4.1.1 on 2022-10-08 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_expert_proof'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expert',
            old_name='proof',
            new_name='fileToUpload',
        ),
    ]
