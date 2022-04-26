from django.urls import path

from provider.views import ProviderListCreateAPIViews
from provider.views import ProviderRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ProviderListCreateAPIViews.as_view(),
         name='provider-create-list'),
    path('<int:id>/', ProviderRetrieveUpdateDestroyAPIView.as_view(),
         name='provider-retrieve-update-delete')
]
