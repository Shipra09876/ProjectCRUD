# Generated by Django 5.0.6 on 2024-09-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passby',
            field=models.CharField(default='', max_length=100),
        ),
    ]
