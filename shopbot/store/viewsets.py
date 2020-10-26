from rest_framework import viewsets ,filters
from .models import Storeitems
from .serializers import StoreitemsSerializer


class StoreitemsViewSet(viewsets.ModelViewSet):
    queryset = Storeitems.objects.all()
    serializer_class = StoreitemsSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('item_id', 'item_name', 'item_qty')