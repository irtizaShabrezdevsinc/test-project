from unicodedata import name
from django.urls import path

from polygon.views import PolygonListCreateAPIViews
from polygon.views import PolygonRetrieveUpdateDestroyAPIView
from polygon.views import PolygonLatLogSearchAPIView


urlpatterns = [
    path('', PolygonListCreateAPIViews.as_view(),
         name='polygon-create-list'),
    path('<int:id>/', PolygonRetrieveUpdateDestroyAPIView.as_view(),
         name='polygon-retrieve-update-delete'),
    path('search/', PolygonLatLogSearchAPIView.as_view(), name='polygon-latlog-search'),
]
