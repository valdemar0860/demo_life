# Generated by Django 4.1.4 on 2023-02-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='title', max_length=255),
        ),
    ]
