# Generated by Django 4.1.3 on 2022-12-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MultiplexCinema",
            fields=[
                ("cinema_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("image_url", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("detail_address", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "multiplex_cinemas",
            },
        ),
    ]
