from django.contrib import admin
from .models import Country, StudentRegistratsion, Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'progname')  
    search_fields = ('progname',)         
    ordering = ('progname',) 

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    search_fields = ('name',)         
    ordering = ('name',)           

@admin.register(StudentRegistratsion)
class StudentAdmin(admin.ModelAdmin):
    # Jadval ustunlari
    list_display = ('id', 'fullname', 'surname', 'email', 'phonenumber', 'country', 'program')  
    # Filtrlash
    list_filter = ('country', 'program')  
     # Qidiruv uchun maydonlar
    search_fields = ('fullname', 'surname', 'email', 'phonenumber') 
   



