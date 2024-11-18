from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Country, Program, StudentRegistratsion
from .serializers import CountrySerializer, ProgramSerializer, StudentSerializer

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class StudentsRegistrationViewSet(ModelViewSet):
    queryset = StudentRegistratsion.objects.all()
    serializer_class = StudentSerializer

