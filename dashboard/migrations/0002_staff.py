# Generated by Django 3.1 on 2020-10-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('empid', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
