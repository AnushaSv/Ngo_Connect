# Generated by Django 4.1.3 on 2024-04-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterNgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('register', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('weurl', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
