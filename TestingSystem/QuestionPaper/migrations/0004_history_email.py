# Generated by Django 4.1.3 on 2023-04-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionPaper', '0003_alter_history_date_alter_history_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
