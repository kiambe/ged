from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

class AbstractViewSet(viewsets.ModelViewSet):
    queryset = Abstract.objects.all()
    serializer_class = AbstractSerializer
    filterset_fields = ['country']

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

class GedDataAPI(APIView):
    def get(self, request, format=None):
        # Get all data from each model
        countries = Country.objects.all()
        organizations = Organization.objects.all()
        regulatory_frameworks = RegulatoryFramework.objects.all()
        ged_organisms = GedOrganism.objects.all()
        abstracts = Abstract.objects.all()
        development_stages = DevelopmentStage.objects.all()
        funding_sources = FundingSource.objects.all()
        human_capacities = HumanCapacity.objects.all()
        equipements = Equipement.objects.all()
        projects = Project.objects.all()
        project_fundings = ProjectFunding.objects.all()
        project_organisms = ProjectOrganism.objects.all()
        country_ged_organisms = CountryGedOrganism.objects.all()
        literatures = Literature.objects.all()

        # Serialize all data
        data = {
            'countries': CountrySerializer(countries, many=True).data,
            'organizations': OrganizationSerializer(organizations, many=True).data,
            'regulatory_frameworks': RegulatoryFrameworkSerializer(regulatory_frameworks, many=True).data,
            'ged_organisms': GedOrganismSerializer(ged_organisms, many=True).data,
            'abstracts': AbstractSerializer(abstracts, many=True).data,
            'development_stages': DevelopmentStageSerializer(development_stages, many=True).data,
            'funding_sources': FundingSourceSerializer(funding_sources, many=True).data,
            'human_capacities': HumanCapacitySerializer(human_capacities, many=True).data,
            'equipements': EquipementSerializer(equipements, many=True).data,
            'projects': ProjectSerializer(projects, many=True).data,
            'project_fundings': ProjectFundingSerializer(project_fundings, many=True).data,
            'project_organisms': ProjectOrganismSerializer(project_organisms, many=True).data,
            'country_ged_organisms': CountryGedOrganismSerializer(country_ged_organisms, many=True).data,
            'literatures': LiteratureSerializer(literatures, many=True).data,
        }

        return Response(data, status=status.HTTP_200_OK)
    


class GedDataByCountryAPI(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        data = []
        
        for country in countries:
            country_data = {
                'country': CountrySerializer(country).data,
                'abstract': AbstractSerializer(country.abstract_set.first()).data if country.abstract_set.exists() else None,
                'organizations': OrganizationSerializer(country.organization_set.all(), many=True).data,
                'regulatory_frameworks': RegulatoryFrameworkSerializer(country.regulatoryframework_set.all(), many=True).data,
                'funding_sources': FundingSourceSerializer(country.fundingsource_set.all(), many=True).data,
                'human_capacity': HumanCapacitySerializer(country.humancapacity_set.first()).data if country.humancapacity_set.exists() else None,
                'projects': ProjectSerializer(country.project_set.all(), many=True).data,
                'country_ged_organisms': CountryGedOrganismSerializer(country.countrygedorganism_set.all(), many=True).data,
                'literatures': LiteratureSerializer(country.literature_set.all(), many=True).data,
            }
            data.append(country_data)
        
        # Add non-country-specific data
        response_data = {
            'by_country': data,
            'ged_organisms': GedOrganismSerializer(GedOrganism.objects.all(), many=True).data,
            'development_stages': DevelopmentStageSerializer(DevelopmentStage.objects.all(), many=True).data,
            'equipements': EquipementSerializer(Equipement.objects.all(), many=True).data,
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
