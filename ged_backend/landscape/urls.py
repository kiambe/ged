from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'regulatory-frameworks', views.RegulatoryFrameworkViewSet)
router.register(r'ged-organisms', views.GedOrganismViewSet)
router.register(r'development-stages', views.DevelopmentStageViewSet)
router.register(r'funding-sources', views.FundingSourceViewSet)
router.register(r'human-capacities', views.HumanCapacityViewSet)
router.register(r'equipements', views.EquipementViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'project-fundings', views.ProjectFundingViewSet)
router.register(r'project-organisms', views.ProjectOrganismViewSet)
router.register(r'country-ged-organisms', views.CountryGedOrganismViewSet)
router.register(r'literature', views.LiteratureViewSet)
router.register(r'abstract', views.AbstractViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('ged-data/', views.GedDataAPI.as_view(), name='ged-data-api'),
    path('ged-country-data/', views.GedDataByCountryAPI.as_view(), name='ged-counytry-data-api'),
]
