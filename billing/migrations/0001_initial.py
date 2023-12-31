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
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=5)),
                ('account_type', models.CharField(choices=[('D', 'Debit'), ('C', 'Credit')], max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientAdmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('package_name', models.CharField(blank=True, max_length=255, null=True)),
                ('insurance_name', models.CharField(blank=True, max_length=255, null=True)),
                ('policy_no', models.CharField(blank=True, max_length=50, null=True)),
                ('agent_name', models.CharField(blank=True, max_length=255, null=True)),
                ('guardian_name', models.CharField(blank=True, max_length=255, null=True)),
                ('guardian_relation', models.CharField(blank=True, max_length=50, null=True)),
                ('guardian_contact', models.CharField(blank=True, max_length=20, null=True)),
                ('guardian_address', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('discount', models.PositiveSmallIntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.service')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('vat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('paid', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('due', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.account')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_method', models.CharField(choices=[('CASH', 'Cash'), ('CARD', 'Card'), ('CHEQUE', 'Cheque')], max_length=6)),
                ('date', models.DateField()),
                ('vat_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('due_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('receipt_no', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.patientadmission')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.doctor')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.service')),
            ],
        ),
        migrations.CreateModel(
            name='AccountPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pay_to', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.BooleanField(default=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.account')),
            ],
        ),
    ]
