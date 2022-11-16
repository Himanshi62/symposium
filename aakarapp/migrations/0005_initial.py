# Generated by Django 4.1 on 2022-09-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("aakarapp", "0004_delete_taskzero"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskZero",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("crid", models.CharField(max_length=10)),
                ("username", models.CharField(max_length=200)),
                ("colgName", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
                ("mobileNo", models.CharField(max_length=10)),
                ("dept", models.CharField(max_length=200)),
                ("whatsappNo", models.CharField(max_length=200)),
                ("pincode", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
    ]
