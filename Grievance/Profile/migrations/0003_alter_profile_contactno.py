# Generated by Django 4.1.3 on 2023-04-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_remove_profile_name_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Contactno',
            field=models.CharField(max_length=12, null=True),
        ),
    ]