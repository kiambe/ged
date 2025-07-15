from django.db import models
from landscape.models import Country

# Funded Projects by Category (Crops, Livestock, etc.)
class ProjectCategory(models.TextChoices):
    CROPS = 'crops', 'Crops'
    LIVESTOCK = 'livestock', 'Livestock'
    MICROBES = 'microbes', 'Microbes/Soil'
    MARINE = 'marine', 'Marine'
    FISHERIES = 'fisheries', 'Fisheries'
    AGROFORESTRY = 'agroforestry', 'Agroforestry'

class FundedProject(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=ProjectCategory.choices)
    count = models.PositiveIntegerField()

# Discriminant Analysis Scores
class DiscriminantScore(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    score_x = models.FloatField()
    score_y = models.FloatField()

# Tier choices
class Tier(models.TextChoices):
    TIER_1 = 'Tier 1', 'Tier 1'
    TIER_2 = 'Tier 2', 'Tier 2'
    TIER_3 = 'Tier 3', 'Tier 3'

# Research Using GEd Technology
class GedResearchScore(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    tier = models.CharField(max_length=10, choices=Tier.choices, blank=True, null=True)
    mean_score = models.FloatField()
    std_error = models.FloatField()

# Equipment Availability Score
class Equipment(models.TextChoices):
    SEQUENCER = 'sequencer', 'Next-Gen Sequencer'
    PCR = 'pcr', 'PCR Machine'
    CENTRIFUGE = 'centrifuge', 'Centrifuge'
    ELECTROPHORESIS = 'electrophoresis', 'Electrophoresis'
    MS = 'ms', 'Mass Spectrophotometer'
    LAMINAR_HOOD = 'laminar_hood', 'Laminar Hood'
    MICROSCOPE = 'microscope', 'Fluorescent Microscope'
    LC = 'lc', 'Liquid Chromatography'
    INCUBATOR = 'incubator', 'Incubator/Shaker'
    OTHERS = 'others', 'Others'

class EquipmentScore(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    tier = models.CharField(max_length=10, choices=Tier.choices, blank=True, null=True)
    equipment = models.CharField(max_length=20, choices=Equipment.choices, blank=True, null=True)
    mean_score = models.FloatField()
    std_error = models.FloatField()

# Knowledge and Experience
class KnowledgeScore(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    mean_score = models.FloatField()
    std_error = models.FloatField()

class ExperienceScore(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    mean_score = models.FloatField()
    std_error = models.FloatField()

# Staff Expertise by Gender
class Gender(models.TextChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'

class Expertise(models.TextChoices):
    ABIOTIC_STRESS = 'abiotic', 'Abiotic Stress'
    BIOTIC_STRESS = 'biotic', 'Biotic Stress'
    ANIMAL_SCIENCE = 'animal', 'Animal Science'
    PLANT_SCIENCE = 'plant', 'Plant Science'
    ENTOMOLOGY = 'entomology', 'Entomology'
    GED_TECHNOLOGY_EFFICIENCY = 'ged_technology_efficiency', 'GEd Technology Efficiency'
    MICROBIOLOGY = 'microbiology', 'Microbiology'
    QUALITY_NUTRITION_TRAITS = 'nutritional', 'Quality Nutritional Traits'
    YIELD_PRODUCTIVITY_TRAITS = 'yield', 'Yield Productivity Traits'
    OTHER = 'other', 'Other'

class StaffExpertise(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    expertise = models.CharField(max_length=30, choices=Expertise.choices)
    count = models.PositiveIntegerField()

# Qualification by Gender
class Qualification(models.TextChoices):
    BSC = 'bsc', 'Bachelor'
    MSC = 'msc', 'Masters'
    PHD = 'phd', 'Doctorate'
    POSTDOC = 'postdoc', 'Postdoc'

class StaffQualification(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    qualification = models.CharField(max_length=20, choices=Qualification.choices)
    count = models.PositiveIntegerField()

# Regulatory Framework
class GraphRegulatoryFramework(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE, related_name='graphs_regulatory_framework')
    biosafety_law = models.CharField(max_length=100, blank=True)
    ministerial_decree = models.CharField(max_length=100, blank=True)
    biosafety_regulations = models.CharField(max_length=100, blank=True)
    ged_guidelines = models.CharField(max_length=100, blank=True)
    ged_apps_received = models.PositiveIntegerField(null=True, blank=True)
    ged_apps_approved = models.PositiveIntegerField(null=True, blank=True)
