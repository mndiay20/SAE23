# Generated by Django 4.2 on 2023-06-02 20:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0006_alter_machine_maintenancedate"),
    ]

    operations = [
        migrations.AddField(
            model_name="machine",
            name="utilisateur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="computerApp.personnel",
            ),
        ),
        migrations.AlterField(
            model_name="machine",
            name="maintenanceDate",
            field=models.DateField(
                default=datetime.datetime(2023, 6, 2, 20, 23, 28, 700728)
            ),
        ),
    ]
