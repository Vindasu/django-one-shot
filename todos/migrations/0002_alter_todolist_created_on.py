# Generated by Django 4.0.5 on 2022-06-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
