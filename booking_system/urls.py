from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('book_now', views.BookNow.as_view(), name='book_now'),
    path('booking_form', views.UserDetails.as_view(), name='booking_form'),
]
