from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryListAPI

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListAPI.as_view()),
    path('<slug:slug>/', include(router.urls))
]
