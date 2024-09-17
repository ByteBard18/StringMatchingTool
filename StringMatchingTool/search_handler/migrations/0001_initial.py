# Generated by Django 4.0 on 2024-09-16 16:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileProcessingResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('query', models.CharField(max_length=255)),
                ('results', models.JSONField()),
            ],
        ),
    ]
