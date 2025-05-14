from django.contrib import admin
from django.utils.html import format_html
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'country_code', 'region')


@admin.register(Organization)
class OrganizationAdmin(ImportExportModelAdmin):
    list_display = ('name', 'country', 'type')  # Removed 'website_link'

    # Uncomment if 'website' field exists in model
    # def website_link(self, obj):
    #     return format_html('<a href="{}" target="_blank">Website</a>', obj.website) if obj.website else "-"
    # website_link.short_description = "Website"


@admin.register(RegulatoryFramework)
class RegulatoryFrameworkAdmin(ImportExportModelAdmin):
    list_display = ('country', 'has_ged_policy', 'year_enacted_published')  # Removed 'last_updated'


@admin.register(Abstract)
class AbstractAdmin(ImportExportModelAdmin):
    list_display = ('country', 'description')  



@admin.register(GedOrganism)
class GedOrganismAdmin(ImportExportModelAdmin):
    list_display = ('common_name', 'scientific_name')  # Removed 'image_preview'

    # Uncomment if 'image' field exists
    # def image_preview(self, obj):
    #     if obj.image:
    #         return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    #     return "-"
    # image_preview.short_description = "Image"


@admin.register(Equipement)
class EquipementAdmin(ImportExportModelAdmin):
    list_display = ('name',)  # Removed 'manufacturer', 'technology_type', 'image_preview'

    # Add back if fields exist and you want custom display
    # def image_preview(self, obj):
    #     if obj.image:
    #         return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    #     return "-"
    # image_preview.short_description = "Image"


@admin.register(DevelopmentStage)
class DevelopmentStageAdmin(ImportExportModelAdmin):
    list_display = ('name',)  # Removed 'order', 'description_short'


@admin.register(FundingSource)
class FundingSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'funding_type')  # Removed 'website_link'


@admin.register(HumanCapacity)
class HumanCapacityAdmin(ImportExportModelAdmin):
    list_display = ('country', 'num_biotech_experts', 'num_gene_editing_specialists', 'num_research_students')
    # Removed 'last_updated'


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('name', 'country')  # Removed 'lead_organization', 'start_date', 'end_date', 'project_duration'


@admin.register(ProjectFunding)
class ProjectFundingAdmin(ImportExportModelAdmin):
    list_display = ('project', 'organization_funding', 'amount_in_usd')  # Removed 'funding_date'


@admin.register(ProjectOrganism)
class ProjectOrganismAdmin(ImportExportModelAdmin):
    list_display = ('project', 'organism', 'technology', 'development_stage')


@admin.register(CountryGedOrganism)
class CountryGedOrganismAdmin(ImportExportModelAdmin):
    list_display = ('country', 'ged_organism', 'status')  # Removed 'status_date'


@admin.register(Literature)
class LiteratureAdmin(ImportExportModelAdmin):
    list_display = ('country',)  # Removed 'title', 'document_type', 'publication_date', 'authors_short'
