# Generated by Django 5.0.2 on 2024-03-05 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PnHyWeb', '0008_alter_student_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportscore',
            old_name='student',
            new_name='student_id',
        ),
    ]