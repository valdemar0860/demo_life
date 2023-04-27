# Generated by Django 4.1.4 on 2023-02-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('is_permanent', models.BooleanField(default=False)),
                ('priority', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
    ]