# Generated by Django 4.1.3 on 2023-05-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_profile_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
