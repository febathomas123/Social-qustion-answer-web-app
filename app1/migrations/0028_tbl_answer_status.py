# Generated by Django 4.1.1 on 2022-11-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_alter_tbl_answer_answer_alter_tbl_answer_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_answer',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
