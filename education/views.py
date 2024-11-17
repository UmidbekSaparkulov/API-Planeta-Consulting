from rest_framework.viewsets import ModelViewSet
from .models import Country, Program, Students_Registratsion
from .serializers import CountrySerializer, ProgramSerializer, StudentSerializer

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class StudentsRegistrationViewSet(ModelViewSet):
    queryset = Students_Registratsion.objects.all()
    serializer_class = StudentSerializer
