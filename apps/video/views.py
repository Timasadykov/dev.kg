from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from apps.video.serializers import VideoSerializer
from apps.video.models import Video


class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticated,)
