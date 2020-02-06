from django.urls import path
from .views import DetailBookView,ListBooksView

urlpatterns = [
    path('',ListBooksView.as_view(),name='book_list'),
    path('<uuid:pk>/',DetailBookView.as_view(),name='book_detail'),
]