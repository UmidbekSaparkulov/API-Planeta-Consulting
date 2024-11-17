from rest_framework import serializers

from .models import Students_Registratsion, Country, Program

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students_Registratsion
        fields = '__all__'


        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

