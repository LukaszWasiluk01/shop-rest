from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer, ProductListSerializer
from .permissions import IsAuthor
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthor,]
    authentication_classes = (TokenAuthentication, SessionAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Product.objects.all()
        slug = self.kwargs.get('slug')
        
        if slug:
            queryset = queryset.filter(category__slug = slug)
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return ProductSerializer
    