# Generated by Django 4.1.3 on 2022-12-31 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cinemas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MultiplexTheater",
            fields=[
                ("theater_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=20)),
                ("seat", models.CharField(max_length=20)),
                (
                    "multiplex_cinema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cinemas.multiplexcinema",
                    ),
                ),
            ],
            options={
                "db_table": "multiplex_theaters",
            },
        ),
    ]
