from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Restaurant, Review, Category, Favorite, Reservation
from .serializers import RestaurantSerializer, ReviewSerializer, CategorySerializer, FavoriteSerializer, ReservationSerializer

class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all().order_by('id')
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description', 'address']
    ordering_fields = ['avg_rating', 'id']
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        restaurant = self.get_object()
        user = request.user
        favorite, created = Favorite.objects.get_or_create(user=user, restaurant=restaurant)
        if not created:
            favorite.delete()
            return Response({'status': 'unfavorited'})
        return Response({'status': 'favorited'})

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, restaurant_id=self.request.data.get('restaurant'))

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class FavoriteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user).order_by('-reservation_date', '-reservation_time')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)