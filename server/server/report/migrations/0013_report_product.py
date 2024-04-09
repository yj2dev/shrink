# Generated by Django 4.1.13 on 2024-01-08 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0015_product_image"),
        ("report", "0012_alter_shrinkflationgeneration_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.product",
            ),
        ),
    ]