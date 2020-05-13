from django.urls import include, path
from rest_framework import routers
from customer import views


router = routers.DefaultRouter()
router.register('_api/create', views.CustomerViewset)
router.register('add', views.BookmarkViewset)
router.register('_api/browse', views.BrowseViewset)

urlpatterns = [
    path('', include(router.urls)),
]
