from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_interface, name='search_interface'),
    path('search/<str:words>/<str:type>', views.click_search, name='click_search'),
]