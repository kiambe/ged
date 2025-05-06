from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_fields = ['region']

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filterset_fields = ['type', 'country']

class RegulatoryFrameworkViewSet(viewsets.ModelViewSet):
    queryset = RegulatoryFramework.objects.all()
    serializer_class = RegulatoryFrameworkSerializer
    filterset_fields = ['country', 'has_ged_policy']

class GedOrganismViewSet(viewsets.ModelViewSet):
    queryset = GedOrganism.objects.all()
    serializer_class = GedOrganismSerializer

class DevelopmentStageViewSet(viewsets.ModelViewSet):
    queryset = DevelopmentStage.objects.all()
    serializer_class = DevelopmentStageSerializer

class FundingSourceViewSet(viewsets.ModelViewSet):
    queryset = FundingSource.objects.all()
    serializer_class = FundingSourceSerializer
    filterset_fields = ['funding_type', 'country']

class HumanCapacityViewSet(viewsets.ModelViewSet):
    queryset = HumanCapacity.objects.all()
    serializer_class = HumanCapacitySerializer

class EquipementViewSet(viewsets.ModelViewSet):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_fields = ['country']

class ProjectFundingViewSet(viewsets.ModelViewSet):
    queryset = ProjectFunding.objects.all()
    serializer_class = ProjectFundingSerializer
    filterset_fields = ['project', 'organization_funding']

class ProjectOrganismViewSet(viewsets.ModelViewSet):
    queryset = ProjectOrganism.objects.all()
    serializer_class = ProjectOrganismSerializer
    filterset_fields = ['project', 'organism']

class CountryGedOrganismViewSet(viewsets.ModelViewSet):
    queryset = CountryGedOrganism.objects.all()
    serializer_class = CountryGedOrganismSerializer
    filterset_fields = ['country', 'ged_organism', 'status']

class LiteratureViewSet(viewsets.ModelViewSet):
    queryset = Literature.objects.all()
    serializer_class = LiteratureSerializer
    filterset_fields = ['country']