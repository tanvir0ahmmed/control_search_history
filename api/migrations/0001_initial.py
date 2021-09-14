# Generated by Django 3.2.7 on 2021-09-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSearchHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('search_keyword', models.JSONField(blank=True, default=dict, null=True)),
                ('searched_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
