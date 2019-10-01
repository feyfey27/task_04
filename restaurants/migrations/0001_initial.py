# Generated by Django 2.1.5 on 2019-10-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('opening_time', models.CharField(max_length=10)),
                ('closing_time', models.CharField(max_length=10)),
            ],
        ),
    ]
