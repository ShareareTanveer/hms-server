# Generated by Django 4.2 on 2023-10-27 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('healthcare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.FileField(blank=True, null=True, upload_to='documents/prescriptions')),
                ('medical_report', models.FileField(blank=True, null=True, upload_to='documents/medical_reports')),
                ('consent_form', models.FileField(blank=True, null=True, upload_to='documents/consent_forms')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='healthcare.doctor')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
            options={
                'verbose_name_plural': 'Patient Documents',
            },
        ),
        migrations.CreateModel(
            name='PatientCseStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_allergies', models.CharField(blank=True, max_length=100, null=True)),
                ('tendency_bleed', models.BooleanField(default=False)),
                ('heart_disease', models.BooleanField(default=False)),
                ('high_blood_pressure', models.BooleanField(default=False)),
                ('diabetic', models.BooleanField(default=False)),
                ('surgery', models.BooleanField(default=False)),
                ('accident', models.BooleanField(default=False)),
                ('others', models.CharField(blank=True, max_length=100, null=True)),
                ('family_medical_history', models.TextField(blank=True, null=True)),
                ('current_medication', models.TextField(blank=True, null=True)),
                ('female_pregnancy', models.BooleanField(default=False)),
                ('breast_feeding', models.BooleanField(default=False)),
                ('health_insurance', models.BooleanField(default=False)),
                ('low_income', models.BooleanField(default=False)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
        ),
    ]
