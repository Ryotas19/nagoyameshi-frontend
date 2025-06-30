from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet, basename='restaurant')
router.register(r'reviews', views.ReviewViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'favorites', views.FavoriteViewSet, basename='favorite')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
