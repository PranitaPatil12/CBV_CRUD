from django.urls import path
from . import views

urlpatterns =[
    path('addM/',views.LaptopView.as_view(),name='lap_add'),
    path('showM/',views.ListView.as_view(),name='lap_show'),
    path('update/<int:i>/',views.UpdateView.as_view(),name='update'),
    path('delete/<int:i>/',views.DeleteView.as_view(),name='delete'),
]