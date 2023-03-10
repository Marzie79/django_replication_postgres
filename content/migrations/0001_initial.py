# Generated by Django 4.1.4 on 2022-12-19 06:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Category id.', primary_key=True, serialize=False, unique=True)),
                ('title', models.TextField(help_text='Category title.', max_length=70, unique=True)),
            ],
        ),
    ]
