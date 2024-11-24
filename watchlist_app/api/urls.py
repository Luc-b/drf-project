from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),
    
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='stream-details'),
    
    path('stream/<int:pk>/rewiew', StreamPlatformAV.as_view(), name='stream-detail'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]