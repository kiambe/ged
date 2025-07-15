# admins.py
from django.contrib import admin
from .models import *

# ────────────────────────────────────────────────────────────────────────────────
#  Helper mixins
# ────────────────────────────────────────────────────────────────────────────────
class CountrySearchMixin:
    """Adds common country search & filter functionality."""
    search_fields = ("country__name",)
    list_filter = ("country",)


# ────────────────────────────────────────────────────────────────────────────────
#  Funded projects
# ────────────────────────────────────────────────────────────────────────────────
@admin.register(FundedProject)
class FundedProjectAdmin(CountrySearchMixin, admin.ModelAdmin):
    list_display = ("country", "category", "count")
    list_filter = ("country", "category")
    list_editable = ("count",)


# ────────────────────────────────────────────────────────────────────────────────
#  Discriminant analysis scores
# ────────────────────────────────────────────────────────────────────────────────
@admin.register(DiscriminantScore)
class DiscriminantScoreAdmin(CountrySearchMixin, admin.ModelAdmin):
    list_display = ("country", "score_x", "score_y")
    list_editable = ("score_x", "score_y")


# ────────────────────────────────────────────────────────────────────────────────
#  GED research scores
# ────────────────────────────────────────────────────────────────────────────────
@admin.register(GedResearchScore)
class GedResearchScoreAdmin(CountrySearchMixin, admin.ModelAdmin):
    list_display = ("country", "tier", "mean_score", "std_error")
    list_filter = ("country", "tier")
    list_editable = ("mean_score", "std_error")


# ────────────────────────────────────────────────────────────────────────────────
#  Equipment scores
# ────────────────────────────────────────────────────────────────────────────────
@admin.register(EquipmentScore)
class EquipmentScoreAdmin(CountrySearchMixin, admin.ModelAdmin):
    list_display = ("country", "tier", "equipment", "mean_score", "std_error")
    list_filter = ("country", "tier", "equipment")
    list_editable = ("mean_score", "std_error")


# ────────────────────────────────────────────────────────────────────────────────
#  Knowledge & experience
# ────────────────────────────────────────────────────────────────────────────────
@admin.register(KnowledgeScore)
class KnowledgeScoreAdmin(CountrySearchMixin, admin.ModelAdmin):
    list_display = ("country", "mean_score", "std_error")
    list_editable = ("mean_score", "std_error")


@admin.register(ExperienceScore)
class ExperienceScoreAdmin(CountrySearchMixin, admin.ModelAdmin):
    list_display = ("country", "mean_score", "std_error")
    list_editable = ("mean_score", "std_error")


# ────────────────────────────────────────────────────────────────────────────────
#  Staff expertise
# ────────────────────────────────────────────────────────────────────────────────
@admin.register(StaffExpertise)
class StaffExpertiseAdmin(CountrySearchMixin, admin.ModelAdmin):
    list_display = ("country", "gender", "expertise", "count")
    list_filter = ("country", "gender", "expertise")
    list_editable = ("count",)


# ────────────────────────────────────────────────────────────────────────────────
#  Staff qualifications
# ────────────────────────────────────────────────────────────────────────────────
@admin.register(StaffQualification)
class StaffQualificationAdmin(CountrySearchMixin, admin.ModelAdmin):
    list_display = ("country", "gender", "qualification", "count")
    list_filter = ("country", "gender", "qualification")
    list_editable = ("count",)


# ────────────────────────────────────────────────────────────────────────────────
#  Regulatory framework
# ────────────────────────────────────────────────────────────────────────────────
@admin.register(GraphRegulatoryFramework)
class GraphRegulatoryFrameworkAdmin(CountrySearchMixin, admin.ModelAdmin):
    list_display = (
        "country",
        "biosafety_law",
        "ministerial_decree",
        "biosafety_regulations",
        "ged_guidelines",
        "ged_apps_received",
        "ged_apps_approved",
    )
    readonly_fields = ("country",)
    list_filter = ("country",)
    search_fields = ("country__name", "biosafety_law", "biosafety_regulations")
