# Generated by Django 4.2.8 on 2024-01-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Events", "0002_alter_eventapplication_event_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventapplication",
            name="event_duration",
            field=models.CharField(max_length=10),
        ),
    ]
