# Generated by Django 5.0.2 on 2024-03-05 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PnHyWeb', '0010_rename_student_id_reportscore_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportscore',
            name='id',
        ),
        migrations.AlterField(
            model_name='reportscore',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='PnHyWeb.student'),
        ),
    ]
