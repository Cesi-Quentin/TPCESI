# Generated by Django 3.0.4 on 2020-03-11 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backoffice', '0002_auto_20200311_1459'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='publication',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='personne',
            name='mail',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]