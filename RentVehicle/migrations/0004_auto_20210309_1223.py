# Generated by Django 3.0.4 on 2021-03-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentVehicle', '0003_auto_20210307_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentvehicle',
            old_name='request_accepted_by',
            new_name='request_responded_by',
        ),
        migrations.AddField(
            model_name='rentvehicle',
            name='request_status',
            field=models.CharField(default='Pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='rentvehicle',
            name='Advance_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rentvehicle',
            name='RentVehicle_Total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]