# Generated by Django 3.2.5 on 2023-11-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='price',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
