# Generated by Django 5.1.3 on 2024-11-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quatity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]