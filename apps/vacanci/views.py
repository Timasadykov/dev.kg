from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from apps.vacanci.serializers import VacanciSerializer
from apps.vacanci.models import Vacanci


class VacanciView(ModelViewSet):
    queryset = Vacanci.objects.all()
    serializer_class = VacanciSerializer
    permission_classes = (IsAuthenticated,)


