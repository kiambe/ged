from rest_framework import serializers
from .models import *

# Basic serializers for nested representations
class CountryBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'country_code', 'region']

class GedOrganismBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = GedOrganism
        fields = ['id', 'common_name', 'scientific_name', 'image']

class DevelopmentStageBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentStage
        fields = ['id', 'name', 'description']

class EquipementBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = ['id', 'name', 'description', 'image']

class OrganizationBasicSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = Organization
        fields = ['id', 'name', 'country_code', 'type', 'focus_area_in_ged']

class ProjectBasicSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'country_code', 'nature_of_partnership', 'status']

# Main serializers
class AbstractSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = Abstract
        fields = '__all__'

class FundingSourceSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = FundingSource
        fields = '__all__'

class HumanCapacitySerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = HumanCapacity
        fields = '__all__'

class RegulatoryFrameworkBasicSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = RegulatoryFramework
        fields = '__all__'

class CountryGedOrganismBasicSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = CountryGedOrganism
        fields = ['id', 'country_code', 'status', 'challenge', 'trait_improvement', 'notes']

class LiteratureSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    
    class Meta:
        model = Literature
        fields = '__all__'

# Complex serializers with relationships
class OrganizationSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountryBasicSerializer(read_only=True)
    
    class Meta:
        model = Organization
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

class CountrySerializer(serializers.ModelSerializer):
    organizations = OrganizationBasicSerializer(many=True, read_only=True)
    regulatoryframeworks = RegulatoryFrameworkBasicSerializer(many=True, read_only=True)
    abstract = AbstractSerializer(read_only=True)
    fundingsources = FundingSourceSerializer(many=True, read_only=True)
    humancapacity = HumanCapacitySerializer(read_only=True)
    projects = ProjectBasicSerializer(many=True, read_only=True)
    countrygedorganisms = CountryGedOrganismBasicSerializer(many=True, read_only=True)
    literatures = LiteratureSerializer(many=True, read_only=True)
    
    class Meta:
        model = Country
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    country = CountryBasicSerializer(read_only=True)
    projectfunding_set = ProjectFundingSerializer(many=True, read_only=True)
    projectorganism_set = ProjectOrganismSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'