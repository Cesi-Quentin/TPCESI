# Generated by Django 3.0.4 on 2020-03-12 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backoffice', '0004_auto_20200312_1114'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='event',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='personne',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='publication',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='personne',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='personne',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
