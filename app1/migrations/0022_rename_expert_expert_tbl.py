# Generated by Django 4.1.1 on 2022-11-02 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_alter_expert_email_alter_user_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='expert',
            new_name='expert_tbl',
        ),
    ]
