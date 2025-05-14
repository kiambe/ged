from rest_framework import serializers
from .models import *

class CountryBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'country_code', 'region']

class GedOrganismBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = GedOrganism
        fields = '__all__'

class AbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abstract
        fields = '__all__'

class FundingSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingSource
        fields = '__all__'


class DevelopmentStageBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentStage
        fields = '__all__'

class HumanCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanCapacity
        fields = '__all__'



class EquipementBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = '__all__'

class OrganizationBasicSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = Organization
        fields = '__all__'

class RegulatoryFrameworkBasicSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = RegulatoryFramework
        fields = '__all__'

class ProjectBasicSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'

# Main serializers with relationships
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        depth = 1

class OrganizationSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountryBasicSerializer(read_only=True)
    
    class Meta:
        model = Organization
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountryBasicSerializer(read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'

class ProjectFundingSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='project.country.country_code', read_only=True)
    project = ProjectBasicSerializer(read_only=True)
    organization_funding = OrganizationBasicSerializer(read_only=True)
    
    class Meta:
        model = ProjectFunding
        fields = '__all__'

class ProjectOrganismSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='project.country.country_code', read_only=True)
    project = ProjectBasicSerializer(read_only=True)
    organism = GedOrganismBasicSerializer(read_only=True)
    technology = EquipementBasicSerializer(read_only=True)
    development_stage = DevelopmentStageBasicSerializer(read_only=True)
    
    class Meta:
        model = ProjectOrganism
        fields = '__all__'

class CountryGedOrganismSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountryBasicSerializer(read_only=True)
    ged_organism = GedOrganismBasicSerializer(read_only=True)
    
    class Meta:
        model = CountryGedOrganism
        fields = '__all__'