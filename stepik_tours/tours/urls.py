from django.urls import path
from tours.views import MainView, DepartureView, TourView, KarantinView

urlpatterns = [
    path('index/', MainView.as_view(), name='index'),
    path('departure/<str:departure>/', DepartureView.as_view(),  name='departure'),
    path('tour/<int:pk>/', TourView.as_view(), name='tour'),
    path('karantin/', KarantinView.as_view(), name='karantin'),
]
