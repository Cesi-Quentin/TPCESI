# Generated by Django 3.0.4 on 2020-03-12 10:14

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_auto_20200311_1600'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='promotion',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='personne',
            old_name='mail',
            new_name='userid',
        ),
        migrations.AddField(
            model_name='promotion',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
