rom django.urls import include,path
from rest_framework import routers
from . import views


#router=routers.DefaultRouter()
#router.register(r'listassets',views.userViewSet.as_view({'get':'list'}),basename='listassets')

urlpatterns=[
    #path('',include(router.urls)),
    path('user/',views.userViewSet.as_view({'get':'list','post':'create'})),
    path('user/<int:pk>/',views.userViewSet.as_view({'delete':'destroy'})),
    path('deposit/',views.depositViewSet.as_view({'get':'list','post':'create'})),
    path('deposit/<int:pk>/',views.depositViewSet.as_view({'delete':'destroy'})),
    path('withdraw/',views.withdrawViewSet.as_view({'get':'list','post':'create'})),
    path('withdraw/<int:pk>/',views.withdrawViewSet.as_view({'delete':'destroy'})),
    path('api-auth/', include('rest_framework.urls' , namespace='rest_framework')),  
    ]