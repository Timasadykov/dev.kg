from rest_framework.routers import DefaultRouter as DR

from apps.vacanci.views import  VacanciView

router = DR()

router.register('event', VacanciView)

urlpatterns = [

]

urlpatterns += router.urls
