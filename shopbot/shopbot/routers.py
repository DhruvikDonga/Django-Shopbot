from rest_framework import routers
from store.viewsets import StoreitemsViewSet


router = routers.DefaultRouter()
router.register(r'storeitem', StoreitemsViewSet)