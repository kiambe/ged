from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country_code = models.CharField(max_length=3, unique=True)
    region = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    ORGANIZATION_TYPE_CHOICES = [
        ('government', 'Government'),
        ('regulatory', 'Regulatory'),
        ('university', 'University'),
        ('research', 'Research'),
        ('private_sector', 'Private Sector'), 
        ('development_agency', 'Development Agency'),       
    ]
    type = models.CharField(
        max_length=20,
        choices=ORGANIZATION_TYPE_CHOICES,
        default='government',  # Optional: Set a default value
        verbose_name='Organization Type' # Optional: Human-readable name for the field
    )
    focus_area_in_ged = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class RegulatoryFramework(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True) 
    country = models.ForeignKey(Country, on_delete=models.CASCADE)     
    KeyAuthorityLegislation = models.TextField(blank=True, null=True)
    has_ged_policy = models.BooleanField(default=False)   
    RegulatorStatus = models.TextField(blank=True, null=True)
    framework_summary = models.TextField(blank=True, null=True)
    year_enacted_published = models.DateField(blank=True, null=True)
    def __str__(self):
        return f"{self.name} Regulatory Framework"

class GedOrganism(models.Model):
    common_name = models.CharField(max_length=255, blank=True, null=True)
    scientific_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return f"{self.common_name} Ged Organism"




class DevelopmentStage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.name} Development Stage"


class FundingSource(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    funding_type = models.CharField(max_length=100, choices=[
        ('Government', 'Government'),
        ('Donor', 'Donor'),
        ('Private', 'Private'),
        ('Multilateral', 'Multilateral'),
    ])
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.country.name})"

class HumanCapacity(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    num_biotech_experts = models.IntegerField(default=0)
    num_gene_editing_specialists = models.IntegerField(default=0)
    num_research_students = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.country.name} Human Capacity"

class Equipement(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return f"{self.name} Equipement"


class Project(models.Model):    
    name = models.CharField(max_length=100, unique=True)
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    nature_of_partnership = models.CharField(max_length=100, unique=True)
    project_duration = models.IntegerField(default=0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.country.name} Project"

class ProjectFunding(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    organization_funding = models.ForeignKey(Organization, on_delete=models.CASCADE)     
    amount_in_usd = models.FloatField(default=0.0)
    def __str__(self):
        return f"{self.project.name} Project Funding"

class ProjectOrganism(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    organism = models.ForeignKey(GedOrganism, on_delete=models.CASCADE)     
    trait = models.CharField(max_length=255, blank=True, null=True)
    technology = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    development_stage = models.ForeignKey(DevelopmentStage, on_delete=models.CASCADE)   
    def __str__(self):
        return f"{self.project.name} Project Organism"



class CountryGedOrganism(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    ged_organism = models.ForeignKey(GedOrganism, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=[
        ('Under Research', 'Under Research'),
        ('In Trials', 'In Trials'),
        ('Approved', 'Approved'),
        ('Potential', 'Potential'),
    ])
    challenge = models.TextField(blank=True, null=True)
    trait_improvement = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.ged_organism.common_name} in {self.country.name}"


class Literature(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    document_file = models.FileField(upload_to='documents/')
    def __str__(self):
        return f"{self.country} Literature"


