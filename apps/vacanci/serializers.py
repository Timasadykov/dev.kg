from rest_framework import serializers

from apps.vacanci.models import Vacanci


class VacanciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacanci
        fields = (
            'name','сompany', 'post','selery', 'type_work', 'description', 'email',
        )