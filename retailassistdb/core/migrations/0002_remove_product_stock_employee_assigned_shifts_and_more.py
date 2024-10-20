# Generated by Django 5.0.7 on 2024-10-20 18:37

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="stock",
        ),
        migrations.AddField(
            model_name="employee",
            name="assigned_shifts",
            field=models.ManyToManyField(
                blank=True, related_name="assigned_employees", to="core.shift"
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="average_transaction_value",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="employee",
            name="performance_score",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name="employee",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="shift_schedule",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scheduled_employees",
                to="core.shift",
            ),
        ),
    ]
