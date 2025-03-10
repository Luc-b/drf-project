from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Dokumentacija",
        default_version="v1",
        description="Ovdje je opis tvog API-ja.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tvojemail@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
     
    path('', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-details'),
    
    path('', include(router.urls)),
    
    path('<int:pk>/reviews/create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),    
    
    path('user-reviews/', views.UserReview.as_view(), name='user-review-detail'),    
]