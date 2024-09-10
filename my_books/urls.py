from  django.urls import path
from .views import book_list, book_list2,book_list3,book,book2
urlpatterns = [
    path('', book_list),
    path('book/1', book_list2),
    path('book/2', book_list3),
    path('book', book),
    path('book2',book2),
]