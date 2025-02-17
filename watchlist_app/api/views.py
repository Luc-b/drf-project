from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, viewsets, filters, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework import mixins

from watchlist_app.api import serializers, pagination, throttling, permissions
from watchlist_app import models

class UserReview(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle, AnonRateThrottle]
    
    # def get_queryset(self):
    #     username = self.kwargs['username'] 
    #     return Review.objects.filter(review_user__username=username)
    
    def get_queryset(self):
        username = self.request.query_params.get('username',None)
        return models.Review.objects.filter(review_user__username=username)

class ReviewCreate(generics.CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [throttling.ReviewCreateThrottle]
    def get_queryset(self):
        return models.Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = models.WatchList.objects.get(pk=pk)
        
        review_user=self.request.user
        review_queryset = models.Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You  have already reviewed this movie.")
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
            
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        
        serializer.save(watchlist=watchlist, review_user=review_user)
    
class ReviewList(generics.ListAPIView):
    
    serializer_class = serializers.ReviewSerializer
    # permission_classes = [IsAuthenticated]
    throttle_classes = [throttling.ReviewListThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']
    
    def get_queryset(self):
        pk = self.kwargs['pk'] 
        return models.Review.objects.filter(watchlist=pk)
        
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.ReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = models.StreamPlatform.objects.all()
    serializer_class = serializers.StreamPlatformSerializer
    permission_classes = [permissions.AdminOrReadOnly]

#only get option
# class StreamPlatformVS(viewsets.ReadOnlyModelViewSet):
    # queryset = StreamPlatform.objects.all()
    # serializer_class = StreamPlatformSerializer

# class StreamPlatformAV(APIView):
#     permission_classes = [permissions.AdminOrReadOnly]
#     def get(self, request):
#         platform = models.StreamPlatform.objects.all()
#         serializer = serializers.StreamPlatformSerializer(platform, many=True, context={'request':request})
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = serializers.StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
            
# class WatchListGV(generics.ListAPIView):
#     queryset = models.WatchList.objects.all()
#     serializer_class = serializers.WatchListSerializer
#     pagination_class = pagination.WatchListCPagination
    
    # filters_backend = [DjangoFilterBackend]
    # filterset_fields = ['title', 'platform__name']
    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['=title', 'platform__name']
    
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['avg_rating']    
        
class WatchListAV(APIView):
    permission_classes = [permissions.AdminOrReadOnly]
    def get(self, request):
        movies = models.WatchList.objects.all()
        serializer = serializers.WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):
    
    permission_classes = [permissions.AdminOrReadOnly]
    def get(self, request,pk):
        try:
            movie = models.WatchList.objects.get(pk=pk)
        except models.WatchList.DoesNotExist:
            return Response({'Error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request,pk):
        movie = models.WatchList.objects.get(pk=pk)
        serializer = serializers.WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = models.WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StreamDetailAV(APIView):
    permission_classes = [permissions.AdminOrReadOnly]
    throttle_classes = [AnonRateThrottle]
    def get(self, request,pk):
        try:
            platform = models.StreamPlatform.objects.get(pk=pk)
        except models.StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request,pk):
        platform = models.StreamPlatform.objects.get(pk=pk)
        serializer = serializers.StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        platform = models.StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)