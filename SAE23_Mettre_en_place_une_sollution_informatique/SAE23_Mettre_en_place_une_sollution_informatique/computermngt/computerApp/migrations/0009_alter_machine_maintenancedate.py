# Generated by Django 4.2 on 2023-06-02 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0008_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 2, 22, 12, 14, 515954)
            ),
        ),
    ]