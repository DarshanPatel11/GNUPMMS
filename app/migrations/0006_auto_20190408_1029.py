# Generated by Django 2.1.7 on 2019-04-08 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190408_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultymaster',
            name='CollegeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster'),
        ),
    ]
