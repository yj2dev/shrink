# Generated by Django 4.1.13 on 2023-12-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_productanalysis_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productanalysis",
            name="image",
            field=models.ImageField(blank=True, upload_to="detect/"),
        ),
    ]
