# Generated by Django 4.1.3 on 2023-04-13 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemuser',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='First_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='Last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
