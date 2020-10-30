# Generated by Django 3.1.2 on 2020-10-27 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20201027_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='schoolprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
