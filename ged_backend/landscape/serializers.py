from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class RegulatoryFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegulatoryFramework
        fields = '__all__'

class GedOrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = GedOrganism
        fields = '__all__'

class AbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abstract
        fields = '__all__'

class DevelopmentStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentStage
        fields = '__all__'

class FundingSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingSource
        fields = '__all__'

class HumanCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanCapacity
        fields = '__all__'

class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectFundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFunding
        fields = '__all__'

class ProjectOrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectOrganism
        fields = '__all__'

class CountryGedOrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryGedOrganism
        fields = '__all__'

class LiteratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Literature
        fields = '__all__'