# Generated by Django 4.2.1 on 2023-06-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_is_preorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo_name',
            field=models.TextField(default='placeholder'),
        ),
    ]
