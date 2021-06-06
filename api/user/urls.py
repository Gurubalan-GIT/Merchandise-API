from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)
urlpatterns = [
    path('login/', views.sign_in, name='sign_in'),
    path('logout/<int:id>/', views.sign_out, name='sign_out'),
    path('', include(router.urls))
]
