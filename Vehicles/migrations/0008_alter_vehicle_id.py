# Generated by Django 4.2.6 on 2023-11-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0007_auto_20210307_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
