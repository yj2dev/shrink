# Generated by Django 4.1.13 on 2024-01-08 06:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("report", "0013_report_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="report",
            name="product_name",
        ),
    ]