# Generated by Django 4.2 on 2023-10-27 08:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_type', models.CharField(choices=[('General', 'General'), ('ICU', 'ICU'), ('NICU', 'NICU')], max_length=50)),
                ('description', models.TextField()),
                ('bed_capacity', models.PositiveIntegerField()),
                ('charge', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('short_bio', ckeditor.fields.RichTextField()),
                ('spacialist', models.CharField(max_length=100)),
                ('education_degree', ckeditor.fields.RichTextField()),
                ('status', models.BooleanField(default=True)),
                ('visiting_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.department')),
                ('user_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('per_patient_time', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('available_days', models.ManyToManyField(related_name='schedules', to='healthcare.day')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='healthcare.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(blank=True, editable=False, max_length=5, null=True, unique=True)),
                ('occupation', models.CharField(max_length=30)),
                ('medical_history', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('user_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='DeathReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('place_of_death', models.CharField(max_length=255)),
                ('cause_of_death', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BirthReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_birth', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('delivery_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BedAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('discharge_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.bed')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('problem', models.TextField()),
                ('time_alloted', models.TimeField()),
                ('serial_no', models.IntegerField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('is_disabled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.department')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
            options={
                'ordering': ['created_at'],
                'get_latest_by': 'created_at',
            },
        ),
    ]
