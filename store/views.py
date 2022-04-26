from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Product.objects.all()
        slug = self.kwargs.get('slug')
        
        if slug:
            queryset = queryset.filter(category__slug = slug)
        return queryset
    