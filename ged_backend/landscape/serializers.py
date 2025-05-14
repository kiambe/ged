from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True
    )
    
    class Meta:
        model = Organization
        fields = '__all__'


class AbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abstract
        fields = '__all__'

class RegulatoryFrameworkSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True
    )
    
    class Meta:
        model = RegulatoryFramework
        fields = '__all__'

class GedOrganismSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = GedOrganism
        fields = '__all__'
    
    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

class DevelopmentStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentStage
        fields = '__all__'

class FundingSourceSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True
    )
    
    class Meta:
        model = FundingSource
        fields = '__all__'

class HumanCapacitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = HumanCapacity
        fields = '__all__'

class EquipementSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Equipement
        fields = '__all__'
    
    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

class ProjectSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True
    )
    
    class Meta:
        model = Project
        fields = '__all__'

class ProjectFundingSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    organization_funding = OrganizationSerializer(read_only=True)
    
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        source='project',
        write_only=True
    )
    organization_funding_id = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(),
        source='organization_funding',
        write_only=True
    )
    
    class Meta:
        model = ProjectFunding
        fields = '__all__'

class ProjectOrganismSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    organism = GedOrganismSerializer(read_only=True)
    technology = EquipementSerializer(read_only=True)
    development_stage = DevelopmentStageSerializer(read_only=True)
    
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        source='project',
        write_only=True
    )
    organism_id = serializers.PrimaryKeyRelatedField(
        queryset=GedOrganism.objects.all(),
        source='organism',
        write_only=True
    )
    technology_id = serializers.PrimaryKeyRelatedField(
        queryset=Equipement.objects.all(),
        source='technology',
        write_only=True
    )
    development_stage_id = serializers.PrimaryKeyRelatedField(
        queryset=DevelopmentStage.objects.all(),
        source='development_stage',
        write_only=True
    )
    
    class Meta:
        model = ProjectOrganism
        fields = '__all__'

class CountryGedOrganismSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    ged_organism = GedOrganismSerializer(read_only=True)
    
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True
    )
    ged_organism_id = serializers.PrimaryKeyRelatedField(
        queryset=GedOrganism.objects.all(),
        source='ged_organism',
        write_only=True
    )
    
    class Meta:
        model = CountryGedOrganism
        fields = '__all__'

class LiteratureSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    document_url = serializers.SerializerMethodField()
    
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country',
        write_only=True
    )
    
    class Meta:
        model = Literature
        fields = '__all__'
    
    def get_document_url(self, obj):
        if obj.document_file:
            return self.context['request'].build_absolute_uri(obj.document_file.url)
        return None




class CombinedCountryDataSerializer(serializers.Serializer):
    # Country data
    country = CountrySerializer()
    
    # Related data
    organizations = OrganizationSerializer(many=True)
    regulatory_frameworks = RegulatoryFrameworkSerializer(many=True)
    funding_sources = FundingSourceSerializer(many=True)
    human_capacity = HumanCapacitySerializer()
    abstract = AbstractSerializer()
    
    # Projects and related data
    projects = serializers.SerializerMethodField()
    
    # Organism data
    country_ged_organisms = serializers.SerializerMethodField()
    literature = LiteratureSerializer(many=True)

    def get_projects(self, obj):
        projects = Project.objects.filter(country=obj)
        project_data = []
        
        for project in projects:
            project_serializer = ProjectSerializer(project)
            project_data.append({
                **project_serializer.data,
                'funding_sources': ProjectFundingSerializer(
                    ProjectFunding.objects.filter(project=project),
                    many=True
                ).data,
                'project_organisms': ProjectOrganismSerializer(
                    ProjectOrganism.objects.filter(project=project),
                    many=True
                ).data
            })
        return project_data

    def get_country_ged_organisms(self, obj):
        organisms = CountryGedOrganism.objects.filter(country=obj)
        organism_data = []
        
        for organism in organisms:
            organism_serializer = CountryGedOrganismSerializer(organism)
            organism_data.append({
                **organism_serializer.data,
                'ged_organism_details': GedOrganismSerializer(
                    organism.ged_organism
                ).data
            })
        return organism_data
