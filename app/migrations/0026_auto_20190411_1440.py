# Generated by Django 2.1.7 on 2019-04-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20190411_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='AddStudentApprovalRights',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ChangeExternalGuideRights',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ChangeInternalGuideRights',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ChangeMentorGuideRights',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='RemoveStudentApprovalRights',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projects',
            name='TermLead',
            field=models.IntegerField(default=0),
        ),
    ]