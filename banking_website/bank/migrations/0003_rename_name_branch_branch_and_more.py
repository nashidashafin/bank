# Generated by Django 4.1.3 on 2023-03-24 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_distric'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='name',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='district',
            new_name='district_id',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='name',
            new_name='district',
        ),
        migrations.DeleteModel(
            name='distric',
        ),
    ]
