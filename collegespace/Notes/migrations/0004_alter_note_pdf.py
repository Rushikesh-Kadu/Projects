# Generated by Django 3.2.5 on 2022-05-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_rename_notes_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdf/'),
        ),
    ]