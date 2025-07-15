from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'funded-projects', FundedProjectViewSet)
router.register(r'discriminant-scores', DiscriminantScoreViewSet)
router.register(r'ged-research-scores', GedResearchScoreViewSet)
router.register(r'equipment-scores', EquipmentScoreViewSet)
router.register(r'knowledge-scores', KnowledgeScoreViewSet)
router.register(r'experience-scores', ExperienceScoreViewSet)
router.register(r'staff-expertise', StaffExpertiseViewSet)
router.register(r'staff-qualification', StaffQualificationViewSet)
router.register(r'regulatory-frameworks', GraphRegulatoryFrameworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]