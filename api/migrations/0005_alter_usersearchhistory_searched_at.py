# Generated by Django 3.2.7 on 2021-09-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_smartphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearchhistory',
            name='searched_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]