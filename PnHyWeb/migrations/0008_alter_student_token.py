# Generated by Django 5.0.2 on 2024-02-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PnHyWeb', '0007_alter_role_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='token',
            field=models.CharField(max_length=2555, null=True),
        ),
    ]
