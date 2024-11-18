from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Program(models.Model):
    progname = models.CharField(max_length=200)

    def __str__(self):
        return self.progname



class StudentRegistratsion(models.Model):
    image = models.ImageField(upload_to='images/student')
    fullname = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=30)
    email = models.EmailField()


    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)


    languagecertif = models.FileField(upload_to='uploads/languagecertificates/', blank=True, null=True)
    greenpassport = models.FileField(upload_to='uploads/greenpassports/', blank=True, null=True)
    zagranpassport = models.FileField(upload_to='uploads/zagranpassports/', blank=True, null=True)
    parentpassport = models.FileField(upload_to='uploads/parentpassports/', blank=True, null=True)
    diploma = models.FileField(upload_to='uploads/diplomas/', blank=True, null=True)
    attestat = models.FileField(upload_to='uploads/attestats/', blank=True, null=True)
    motivationletter = models.FileField(upload_to='uploads/motivation_letters/', blank=True, null=True)
    recommendationletter = models.FileField(upload_to='uploads/recommendation_letters/', blank=True, null=True)
    parentjobcertificate = models.FileField(upload_to='uploads/parent_job_certificates/', blank=True, null=True)
    apostille = models.FileField(upload_to='uploads/apostilles/', blank=True, null=True)
    dov = models.FileField(upload_to='uploads/dovdocuments/', blank=True, null=True)
    insurance = models.FileField(upload_to='uploads/insurances/', blank=True, null=True)
    bankaccount = models.FileField(upload_to='uploads/bankaccounts/', blank=True, null=True)
    visa = models.FileField(upload_to='uploads/visas/', blank=True, null=True)



    def __str__(self):
        return f"{self.fullname} {self.surname}"


