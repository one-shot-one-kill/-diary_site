# Generated by Django 4.0.4 on 2022-05-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('data_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['data_created'],
            },
        ),
    ]
