from django.urls import path, include

from rest_framework import routers

from . import view_sets, views

app_name = 'coffee_shop_api_v1'

router = routers.DefaultRouter()
router.register(r'coffee_machines', view_sets.CoffeeMachineViewSet)
router.register(r'coffee_pods', view_sets.CoffeePodViewSet)

urlpatterns = [
    path('populate_data/', views.PopulateData.as_view(), name='populate_data'),
    path('', include(router.urls)),
]
