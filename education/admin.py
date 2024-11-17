from django.contrib import admin
from .models import Country, Students_Registratsion, Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'prog_name')  
    search_fields = ('prog_name',)         
    ordering = ('prog_name',) 

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    search_fields = ('name',)         
    ordering = ('name',)           

@admin.register(Students_Registratsion)
class StudentAdmin(admin.ModelAdmin):
    # Jadval ustunlari
    list_display = ('id', 'full_name', 'surname', 'email', 'phone_number', 'country', 'program')  
    # Filtrlash
    list_filter = ('country', 'program')  
     # Qidiruv uchun maydonlar
    search_fields = ('full_name', 'surname', 'email', 'phone_number') 
   


