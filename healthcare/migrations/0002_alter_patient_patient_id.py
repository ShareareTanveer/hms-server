# Generated by Django 4.2 on 2023-10-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(blank=True, editable=False, max_length=5, null=True, unique=True),
        ),
    ]
