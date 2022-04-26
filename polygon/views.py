from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from polygon.models import Polygon

from polygon.serializer import PolygonSerializer, PolygonLatLogSerializer


class PolygonListCreateAPIViews(ListCreateAPIView):
    serializer_class = PolygonSerializer
    queryset = Polygon.objects.all()


class PolygonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PolygonSerializer
    queryset = Polygon.objects.all()
    lookup_field = 'id'


class PolygonLatLogSearchAPIView(GenericAPIView):
    serializer_class = PolygonLatLogSerializer
    def post(self, request):
        print(request.data);
        polygon = Polygon.objects.filter(longitude = request.data['longitude'], latitude=request.data['latitude']);
        serializer = PolygonSerializer(polygon, many=True)
        return Response(serializer.data)