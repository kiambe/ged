from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Prefetch
from .models import *
from .serializers import *

class AbstractViewSet(viewsets.ModelViewSet):
    queryset = Abstract.objects.select_related('country')
    serializer_class = AbstractSerializer
    filterset_fields = ['country']

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.prefetch_related(
        Prefetch('organization_set', queryset=Organization.objects.all()),
        Prefetch('regulatoryframework_set', queryset=RegulatoryFramework.objects.all()),
        Prefetch('fundingsource_set', queryset=FundingSource.objects.all()),
        Prefetch('project_set', queryset=Project.objects.all()),
        Prefetch('countrygedorganism_set', queryset=CountryGedOrganism.objects.all()),
        'literature_set'
    ).select_related('abstract', 'humancapacity')
    serializer_class = CountrySerializer
    filterset_fields = ['region']

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.select_related('country')
    serializer_class = OrganizationSerializer
    filterset_fields = ['type', 'country']

class RegulatoryFrameworkViewSet(viewsets.ModelViewSet):
    queryset = RegulatoryFramework.objects.select_related('country')
    serializer_class = RegulatoryFrameworkBasicSerializer
    filterset_fields = ['country', 'has_ged_policy']

class GedOrganismViewSet(viewsets.ModelViewSet):
    queryset = GedOrganism.objects.all()
    serializer_class = GedOrganismBasicSerializer

class DevelopmentStageViewSet(viewsets.ModelViewSet):
    queryset = DevelopmentStage.objects.all()
    serializer_class = DevelopmentStageBasicSerializer

class FundingSourceViewSet(viewsets.ModelViewSet):
    queryset = FundingSource.objects.select_related('country')
    serializer_class = FundingSourceSerializer
    filterset_fields = ['funding_type', 'country']

class HumanCapacityViewSet(viewsets.ModelViewSet):
    queryset = HumanCapacity.objects.select_related('country')
    serializer_class = HumanCapacitySerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.select_related('country').prefetch_related(
        Prefetch('projectfunding_set', 
                queryset=ProjectFunding.objects.select_related('organization_funding')),
        Prefetch('projectorganism_set',
                queryset=ProjectOrganism.objects.select_related(
                    'organism', 'technology', 'development_stage'))
    )
    serializer_class = ProjectSerializer
    filterset_fields = ['country']

class ProjectFundingViewSet(viewsets.ModelViewSet):
    queryset = ProjectFunding.objects.select_related(
        'project', 'project__country', 'organization_funding'
    )
    serializer_class = ProjectFundingSerializer
    filterset_fields = ['project', 'organization_funding']

class ProjectOrganismViewSet(viewsets.ModelViewSet):
    queryset = ProjectOrganism.objects.select_related(
        'project', 'project__country', 'organism', 
        'technology', 'development_stage'
    )
    serializer_class = ProjectOrganismSerializer
    filterset_fields = ['project', 'organism']

class CountryGedOrganismViewSet(viewsets.ModelViewSet):
    queryset = CountryGedOrganism.objects.select_related('country', 'ged_organism')
    serializer_class = CountryGedOrganismBasicSerializer
    filterset_fields = ['country', 'ged_organism', 'status']

class LiteratureViewSet(viewsets.ModelViewSet):
    queryset = Literature.objects.select_related('country')
    serializer_class = LiteratureSerializer
    filterset_fields = ['country']

class GedDataAPI(APIView):
    def get(self, request, format=None):
        # Optimize all queries
        countries = Country.objects.prefetch_related(
            Prefetch('organization_set', queryset=Organization.objects.all()),
            Prefetch('regulatoryframework_set', queryset=RegulatoryFramework.objects.all()),
            Prefetch('fundingsource_set', queryset=FundingSource.objects.all()),
            Prefetch('project_set', queryset=Project.objects.all()),
            Prefetch('countrygedorganism_set', queryset=CountryGedOrganism.objects.all()),
            'literature_set'
        ).select_related('abstract', 'humancapacity')

        projects = Project.objects.select_related('country').prefetch_related(
            Prefetch('projectfunding_set', 
                   queryset=ProjectFunding.objects.select_related('organization_funding')),
            Prefetch('projectorganism_set',
                   queryset=ProjectOrganism.objects.select_related(
                       'organism', 'technology', 'development_stage'))
        )

        # Serialize data
        serialized_data = {
            'countries': CountrySerializer(countries, many=True).data,
            'projects': ProjectSerializer(projects, many=True).data,
            'organizations': OrganizationSerializer(
                Organization.objects.select_related('country'), many=True).data,
            'regulatory_frameworks': RegulatoryFrameworkBasicSerializer(
                RegulatoryFramework.objects.select_related('country'), many=True).data,
            'ged_organisms': GedOrganismBasicSerializer(
                GedOrganism.objects.all(), many=True).data,
            'development_stages': DevelopmentStageBasicSerializer(
                DevelopmentStage.objects.all(), many=True).data,
            'equipements': EquipementBasicSerializer(
                Equipement.objects.all(), many=True).data,
            'funding_sources': FundingSourceSerializer(
                FundingSource.objects.select_related('country'), many=True).data,
            'human_capacities': HumanCapacitySerializer(
                HumanCapacity.objects.select_related('country'), many=True).data,
            'project_fundings': ProjectFundingSerializer(
                ProjectFunding.objects.select_related('project', 'organization_funding'), 
                many=True).data,
            'project_organisms': ProjectOrganismSerializer(
                ProjectOrganism.objects.select_related(
                    'project', 'organism', 'technology', 'development_stage'),
                many=True).data,
            'country_ged_organisms': CountryGedOrganismBasicSerializer(
                CountryGedOrganism.objects.select_related('country', 'ged_organism'), 
                many=True).data,
            'literatures': LiteratureSerializer(
                Literature.objects.select_related('country'), many=True).data,
        }

        return Response(serialized_data, status=status.HTTP_200_OK)