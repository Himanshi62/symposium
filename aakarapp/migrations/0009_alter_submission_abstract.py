# Generated by Django 4.1 on 2022-11-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aakarapp", "0008_submission_delete_taskone_delete_taskzero"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="abstract",
            field=models.FileField(upload_to="doc/"),
        ),
    ]
