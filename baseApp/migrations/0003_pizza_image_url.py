# Generated by Django 4.0.7 on 2023-11-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_pizza'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]