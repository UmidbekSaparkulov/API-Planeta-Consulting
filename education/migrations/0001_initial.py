# Generated by Django 5.1.3 on 2024-11-17 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Students_Registratsion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/student')),
                ('full_name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('language_certificate', models.FileField(blank=True, null=True, upload_to='uploads/language_certificates/')),
                ('green_passport', models.FileField(blank=True, null=True, upload_to='uploads/green_passports/')),
                ('zagran_passport', models.FileField(blank=True, null=True, upload_to='uploads/zagran_passports/')),
                ('parent_passport', models.FileField(blank=True, null=True, upload_to='uploads/parent_passports/')),
                ('diploma', models.FileField(blank=True, null=True, upload_to='uploads/diplomas/')),
                ('attestat', models.FileField(blank=True, null=True, upload_to='uploads/attestats/')),
                ('motivation_letter', models.FileField(blank=True, null=True, upload_to='uploads/motivation_letters/')),
                ('recommendation_letter', models.FileField(blank=True, null=True, upload_to='uploads/recommendation_letters/')),
                ('parent_job_certificate', models.FileField(blank=True, null=True, upload_to='uploads/parent_job_certificates/')),
                ('apostille', models.FileField(blank=True, null=True, upload_to='uploads/apostilles/')),
                ('dov', models.FileField(blank=True, null=True, upload_to='uploads/dov_documents/')),
                ('insurance', models.FileField(blank=True, null=True, upload_to='uploads/insurances/')),
                ('bank_account', models.FileField(blank=True, null=True, upload_to='uploads/bank_accounts/')),
                ('visa', models.FileField(blank=True, null=True, upload_to='uploads/visas/')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.country')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.program')),
            ],
        ),
    ]
