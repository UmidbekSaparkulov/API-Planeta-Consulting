# Generated by Django 5.1.3 on 2024-11-18 03:53

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
                ('progname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegistratsion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/student')),
                ('fullname', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('phonenumber', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('languagecertif', models.FileField(blank=True, null=True, upload_to='uploads/languagecertificates/')),
                ('greenpassport', models.FileField(blank=True, null=True, upload_to='uploads/greenpassports/')),
                ('zagranpassport', models.FileField(blank=True, null=True, upload_to='uploads/zagranpassports/')),
                ('parentpassport', models.FileField(blank=True, null=True, upload_to='uploads/parentpassports/')),
                ('diploma', models.FileField(blank=True, null=True, upload_to='uploads/diplomas/')),
                ('attestat', models.FileField(blank=True, null=True, upload_to='uploads/attestats/')),
                ('motivationletter', models.FileField(blank=True, null=True, upload_to='uploads/motivation_letters/')),
                ('recommendationletter', models.FileField(blank=True, null=True, upload_to='uploads/recommendation_letters/')),
                ('parentjobcertificate', models.FileField(blank=True, null=True, upload_to='uploads/parent_job_certificates/')),
                ('apostille', models.FileField(blank=True, null=True, upload_to='uploads/apostilles/')),
                ('dov', models.FileField(blank=True, null=True, upload_to='uploads/dovdocuments/')),
                ('insurance', models.FileField(blank=True, null=True, upload_to='uploads/insurances/')),
                ('bankaccount', models.FileField(blank=True, null=True, upload_to='uploads/bankaccounts/')),
                ('visa', models.FileField(blank=True, null=True, upload_to='uploads/visas/')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='educationSchool.country')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='educationSchool.program')),
            ],
        ),
    ]
