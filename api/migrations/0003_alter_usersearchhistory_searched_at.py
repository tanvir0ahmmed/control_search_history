# Generated by Django 3.2.7 on 2021-09-13 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210913_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearchhistory',
            name='searched_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
