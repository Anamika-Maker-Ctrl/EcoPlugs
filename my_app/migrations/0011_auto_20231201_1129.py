# Generated by Django 3.2.5 on 2023-12-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_super_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='license_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service_reg',
            name='license_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='station',
            name='license_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
