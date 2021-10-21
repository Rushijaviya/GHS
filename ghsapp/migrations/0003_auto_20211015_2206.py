# Generated by Django 3.2.8 on 2021-10-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghsapp', '0002_auto_20211015_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorinfo',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='age',
        ),
        migrations.AddField(
            model_name='doctorinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
