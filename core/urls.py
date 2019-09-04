from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'result/<int:year>/<str:result>/',
        views.ResultView.as_view(),
        name='result'
    ),
]
