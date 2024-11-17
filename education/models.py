from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Program(models.Model):
    prog_name = models.CharField(max_length=200)

    def __str__(self):
        return self.prog_name



class Students_Registratsion(models.Model):
    image = models.ImageField(upload_to='images/student')
    full_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()


    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)


    language_certificate = models.FileField(upload_to='uploads/language_certificates/', blank=True, null=True)
    green_passport = models.FileField(upload_to='uploads/green_passports/', blank=True, null=True)
    zagran_passport = models.FileField(upload_to='uploads/zagran_passports/', blank=True, null=True)
    parent_passport = models.FileField(upload_to='uploads/parent_passports/', blank=True, null=True)
    diploma = models.FileField(upload_to='uploads/diplomas/', blank=True, null=True)
    attestat = models.FileField(upload_to='uploads/attestats/', blank=True, null=True)
    motivation_letter = models.FileField(upload_to='uploads/motivation_letters/', blank=True, null=True)
    recommendation_letter = models.FileField(upload_to='uploads/recommendation_letters/', blank=True, null=True)
    parent_job_certificate = models.FileField(upload_to='uploads/parent_job_certificates/', blank=True, null=True)
    apostille = models.FileField(upload_to='uploads/apostilles/', blank=True, null=True)
    dov = models.FileField(upload_to='uploads/dov_documents/', blank=True, null=True)
    insurance = models.FileField(upload_to='uploads/insurances/', blank=True, null=True)
    bank_account = models.FileField(upload_to='uploads/bank_accounts/', blank=True, null=True)
    visa = models.FileField(upload_to='uploads/visas/', blank=True, null=True)



    def __str__(self):
        return f"{self.full_name} {self.surname}"

