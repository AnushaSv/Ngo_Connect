# Generated by Django 4.1.3 on 2024-03-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='confirmpass',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
