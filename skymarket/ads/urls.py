from django.urls import include, path
from rest_framework import routers

from skymarket.ads.views import AdViewSet, CommentViewSet

ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet)
ads_router.register('ads/(?P<ad_id>[^/.]+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(ads_router.urls)),
]
