from  django.urls import path
from .views import book_list, book_list2,book_list3,book_list4,book,book2,book3
urlpatterns = [
    path('', book_list),
    path('book/1', book_list2),
    path('book/2', book_list3),
    path('book/3', book_list4),
    path('book', book),
    path('book2',book2),
    path('book3',book3)
]