from django.urls import include, path
from rest_framework import routers
from customer import views


router = routers.DefaultRouter()
router.register('_api/create', views.CustomerViewset)
router.register('add', views.BookmarkViewSet)
router.register('_api/browse', views.BrowseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
