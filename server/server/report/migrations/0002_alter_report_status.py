# Generated by Django 4.1.13 on 2023-12-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("report", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="status",
            field=models.IntegerField(
                choices=[(1, "접수"), (2, "처리중"), (3, "완료")], default=1
            ),
        ),
    ]
