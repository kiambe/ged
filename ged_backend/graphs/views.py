from rest_framework import viewsets
from .models import *
from .serializers import *

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class FundedProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FundedProject.objects.all()
    serializer_class = FundedProjectSerializer

class DiscriminantScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DiscriminantScore.objects.all()
    serializer_class = DiscriminantScoreSerializer

class GedResearchScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GedResearchScore.objects.all()
    serializer_class = GedResearchScoreSerializer

class EquipmentScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EquipmentScore.objects.all()
    serializer_class = EquipmentScoreSerializer

class KnowledgeScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = KnowledgeScore.objects.all()
    serializer_class = KnowledgeScoreSerializer

class ExperienceScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExperienceScore.objects.all()
    serializer_class = ExperienceScoreSerializer

class StaffExpertiseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StaffExpertise.objects.all()
    serializer_class = StaffExpertiseSerializer

class StaffQualificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StaffQualification.objects.all()
    serializer_class = StaffQualificationSerializer

class GraphRegulatoryFrameworkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GraphRegulatoryFramework.objects.all()
    serializer_class = GraphRegulatoryFrameworkSerializer
