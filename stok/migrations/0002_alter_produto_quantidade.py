# Generated by Django 5.2 on 2025-04-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(max_length=10),
        ),
    ]
