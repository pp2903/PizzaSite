# Generated by Django 5.0 on 2024-01-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseApp", "0007_alter_orderitem_item_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]