# Generated by Django 4.2.5 on 2023-09-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_alter_answer_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
