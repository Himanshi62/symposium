# Generated by Django 4.1 on 2022-11-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aakarapp', '0007_taskone_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('colgName', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('mobileNo', models.IntegerField(max_length=10)),
                ('co1', models.CharField(max_length=200)),
                ('mail1', models.CharField(max_length=100)),
                ('co2', models.CharField(max_length=200)),
                ('mail2', models.CharField(max_length=100)),
                ('co3', models.CharField(max_length=200)),
                ('mail3', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('others', models.CharField(max_length=100)),
                ('abstract', models.CharField(max_length=100)),
                ('authentication', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='TaskOne',
        ),
        migrations.DeleteModel(
            name='TaskZero',
        ),
    ]
