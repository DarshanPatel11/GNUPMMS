# Generated by Django 2.1.7 on 2019-04-10 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20190410_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stageactivities',
            name='Status',
            field=models.IntegerField(choices=[(-1, 'Pending'), (0, 'Approval Pending'), (1, 'Approved')]),
        ),
    ]
