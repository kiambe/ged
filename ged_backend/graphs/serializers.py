from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class FundedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundedProject
        fields = '__all__'

class DiscriminantScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscriminantScore
        fields = '__all__'

class GedResearchScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GedResearchScore
        fields = '__all__'

class EquipmentScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentScore
        fields = '__all__'

class KnowledgeScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeScore
        fields = '__all__'

class ExperienceScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceScore
        fields = '__all__'

class StaffExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffExpertise
        fields = '__all__'

class StaffQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffQualification
        fields = '__all__'

class GraphRegulatoryFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphRegulatoryFramework
        fields = '__all__'