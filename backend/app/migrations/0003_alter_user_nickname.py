# Generated by Django 4.2.16 on 2024-11-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
