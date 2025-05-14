from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Prefetch

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
    serializer_class = RegulatoryFrameworkBasicSerializer
    filterset_fields = ['country', 'has_ged_policy']

class GedOrganismViewSet(viewsets.ModelViewSet):
    queryset = GedOrganism.objects.all()
    serializer_class = GedOrganismBasicSerializer

class DevelopmentStageViewSet(viewsets.ModelViewSet):
    queryset = DevelopmentStage.objects.all()
    serializer_class = DevelopmentStageBasicSerializer

class FundingSourceViewSet(viewsets.ModelViewSet):
    queryset = FundingSource.objects.all()
    serializer_class = FundingSourceSerializer
    filterset_fields = ['funding_type', 'country']

class HumanCapacityViewSet(viewsets.ModelViewSet):
    queryset = HumanCapacity.objects.all()
    serializer_class = HumanCapacitySerializer


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

# class LiteratureViewSet(viewsets.ModelViewSet):
#     queryset = Literature.objects.all()
#     serializer_class = LiteratureSerializer
#     filterset_fields = ['country']

class GedDataAPI(APIView):
    def get(self, request, format=None):
        # Optimize queries to prevent N+1 problems
        projects_prefetch = Prefetch(
            'projectorganism_set',
            queryset=ProjectOrganism.objects.select_related(
                'organism', 'technology', 'development_stage'
            )
        )
        
        fundings_prefetch = Prefetch(
            'projectfunding_set',
            queryset=ProjectFunding.objects.select_related('organization_funding')
        )
        
        # Get all data with optimized queries
        data = {
            'countries': Country.objects.prefetch_related(
                'organization_set',
                'regulatoryframework_set',
                'abstract_set',
                'fundingsource_set',
                'humancapacity_set',
                'project_set',
                'countrygedorganism_set',
                'literature_set'
            ),
            'organizations': Organization.objects.select_related('country'),
            'regulatory_frameworks': RegulatoryFramework.objects.select_related('country'),
            'ged_organisms': GedOrganism.objects.all(),
            'abstracts': Abstract.objects.select_related('country'),
            'development_stages': DevelopmentStage.objects.all(),
            'funding_sources': FundingSource.objects.select_related('country'),
            'human_capacities': HumanCapacity.objects.select_related('country'),
            'equipements': Equipement.objects.all(),
            'projects': Project.objects.select_related('country')
                        .prefetch_related(projects_prefetch, fundings_prefetch),
            'project_fundings': ProjectFunding.objects.select_related(
                'project', 'project__country', 'organization_funding'
            ),
            'project_organisms': ProjectOrganism.objects.select_related(
                'project', 'project__country', 'organism', 
                'technology', 'development_stage'
            ),
            'country_ged_organisms': CountryGedOrganism.objects.select_related(
                'country', 'ged_organism'
            ),
            'literatures': Literature.objects.select_related('country'),
        }

        # Serialize data without recursion
        serialized_data = {
            'countries': CountrySerializer(data['countries'], many=True).data,
            'organizations': OrganizationSerializer(data['organizations'], many=True).data,
            'regulatory_frameworks': RegulatoryFrameworkBasicSerializer(
                data['regulatory_frameworks'], many=True).data,
            'ged_organisms': GedOrganismBasicSerializer(data['ged_organisms'], many=True).data,
            'abstracts': AbstractSerializer(data['abstracts'], many=True).data,
            'development_stages': DevelopmentStageBasicSerializer(
                data['development_stages'], many=True).data,
            'funding_sources': FundingSourceSerializer(data['funding_sources'], many=True).data,
            'human_capacities': HumanCapacitySerializer(
                data['human_capacities'], many=True).data,
            'equipements': EquipementBasicSerializer(data['equipements'], many=True).data,
            'projects': ProjectSerializer(data['projects'], many=True).data,
            'project_fundings': ProjectFundingSerializer(
                data['project_fundings'], many=True).data,
            'project_organisms': ProjectOrganismSerializer(
                data['project_organisms'], many=True).data,
            'country_ged_organisms': CountryGedOrganismSerializer(
                data['country_ged_organisms'], many=True).data,
            # 'literatures': LiteratureSerializer(data['literatures'], many=True).data,
        }

        return Response(serialized_data, status=status.HTTP_200_OK)