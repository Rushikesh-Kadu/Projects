# Generated by Django 3.2.5 on 2022-05-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quepaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstsem1',
            name='pdf',
            field=models.FileField(upload_to='static/pdf/'),
        ),
        migrations.AlterField(
            model_name='firstsem2',
            name='pdf',
            field=models.FileField(upload_to='static/pdf/'),
        ),
        migrations.AlterField(
            model_name='secondsem1',
            name='pdf',
            field=models.FileField(upload_to='static/pdf/'),
        ),
        migrations.AlterField(
            model_name='secondsem2',
            name='pdf',
            field=models.FileField(upload_to='static/pdf/'),
        ),
        migrations.AlterField(
            model_name='thirdsem1',
            name='pdf',
            field=models.FileField(upload_to='static/pdf/'),
        ),
        migrations.AlterField(
            model_name='thirdsem2',
            name='pdf',
            field=models.FileField(upload_to='static/pdf/'),
        ),
    ]
