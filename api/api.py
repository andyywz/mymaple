from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Daily
from .serializers import DailySerializer

class DailyViewSet(viewsets.ModelViewSet):
    serializer_class = DailySerializer
    queryset = Daily.objects.all()
    permission_classes = []

    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        daily = self.get_object()
        if daily.completed:
            daily.reset()
            return Response({ 'status': '%s marked incomplete' %(daily.title) })
        else:
            daily.complete()
            return Response({ 'status': '%s marked complete %s' %(daily.title, daily.completed_at) })
