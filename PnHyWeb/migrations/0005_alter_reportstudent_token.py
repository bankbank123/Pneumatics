# Generated by Django 5.0.2 on 2024-02-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PnHyWeb', '0004_remove_reportstudent_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportstudent',
            name='token',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
