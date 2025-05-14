from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class GedOrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = GedOrganism
        fields = '__all__'

class DevelopmentStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentStage
        fields = '__all__'

class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = Organization
        fields = '__all__'

class RegulatoryFrameworkSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = RegulatoryFramework
        fields = '__all__'

class AbstractSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = Abstract
        fields = '__all__'

class FundingSourceSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = FundingSource
        fields = '__all__'

class HumanCapacitySerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = HumanCapacity
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountrySerializer(read_only=True)
    organizations = serializers.SerializerMethodField()
    fundings = serializers.SerializerMethodField()
    organisms = serializers.SerializerMethodField()
    
    def get_organizations(self, obj):
        fundings = ProjectFunding.objects.filter(project=obj)
        orgs = [funding.organization_funding for funding in fundings]
        return OrganizationSerializer(orgs, many=True).data
    
    def get_fundings(self, obj):
        fundings = ProjectFunding.objects.filter(project=obj)
        return ProjectFundingSerializer(fundings, many=True).data
    
    def get_organisms(self, obj):
        organisms = ProjectOrganism.objects.filter(project=obj)
        return ProjectOrganismSerializer(organisms, many=True).data
    
    class Meta:
        model = Project
        fields = '__all__'

class ProjectFundingSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='project.country.country_code', read_only=True)
    project = ProjectSerializer(read_only=True)
    organization_funding = OrganizationSerializer(read_only=True)
    
    class Meta:
        model = ProjectFunding
        fields = '__all__'

class ProjectOrganismSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='project.country.country_code', read_only=True)
    project = ProjectSerializer(read_only=True)
    organism = GedOrganismSerializer(read_only=True)
    technology = EquipementSerializer(read_only=True)
    development_stage = DevelopmentStageSerializer(read_only=True)
    
    class Meta:
        model = ProjectOrganism
        fields = '__all__'

class CountryGedOrganismSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountrySerializer(read_only=True)
    ged_organism = GedOrganismSerializer(read_only=True)
    
    class Meta:
        model = CountryGedOrganism
        fields = '__all__'

class LiteratureSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country.country_code', read_only=True)
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = Literature
        fields = '__all__'