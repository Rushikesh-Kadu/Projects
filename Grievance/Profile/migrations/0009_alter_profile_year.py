# Generated by Django 4.2.2 on 2023-07-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_alter_profile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Year',
            field=models.CharField(max_length=50),
        ),
    ]