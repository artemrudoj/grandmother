# Generated by Django 2.0.7 on 2018-07-21 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='initial_ration',
            new_name='initial_ratio',
        ),
    ]
