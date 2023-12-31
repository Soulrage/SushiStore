# Generated by Django 4.1.3 on 2023-02-05 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.TextField(blank=True)),
                ("type", models.TextField(blank=True)),
                ("price", models.IntegerField()),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Users",
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
                ("login", models.TextField(blank=True)),
                ("password", models.TextField(blank=True)),
                ("name", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Basket",
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
                ("count", models.IntegerField()),
                ("sum_price", models.IntegerField()),
                (
                    "manu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="restoran.menu"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="restoran.users"
                    ),
                ),
            ],
        ),
    ]
