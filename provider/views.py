from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from provider.models import Provider


from provider.serializer import ProviderSerializer


class ProviderListCreateAPIViews(ListCreateAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ProviderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    lookup_field = 'id'
