# Generated by Django 4.1.5 on 2023-03-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0005_remove_master_confirmpassword_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='confirmpassword',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='confirmpassword',
            field=models.CharField(default='', max_length=20),
        ),
    ]
