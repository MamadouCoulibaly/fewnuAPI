#importation BlogUserRudView, BlogUserAPIView,BlogUserListAPIView,BlogDepensesRudView,BlogDepensesAPIView,BlogDepensesListAPIView, BlogPretsRudView, BlogPretsAPIView,BlogPretsListAPIView
from .views import *
from django.urls import path


app_name='APIREST'
urlpatterns = [

    path('addvente/', BlogVentesAPIView.as_view(), name='user-create'),
    path('all/', BlogVentesAPIView.as_view(), name='user-listcreate'),
    path('<int:pk>', BlogVentesRudView.as_view(), name='user-rud'),


    path('addepense/', BlogDepensesAPIView.as_view(), name='user-create'),
    path('alldep/', BlogDepensesListAPIView.as_view(), name='user-listcreate'),
    path('<int:pk>', BlogDepensesRudView.as_view(), name='user-rud'),


    path('addpret', BlogPretsAPIView.as_view(), name='user-create'),
    path('allpret/', BlogPretsListAPIView.as_view(), name='user-listcreate'),
    path('<int:pk>', BlogPretsRudView.as_view(), name='user-rud'),

    path('', BlogUsersAPIView.as_view(), name='user-create'),
    path('allusers/', BlogUsersListAPIView.as_view(), name='user-listcreate'),
    path('<int:pk>', BlogUsersRudView.as_view(), name='user-rud'),

]