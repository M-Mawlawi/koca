from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    path('exam/<int:quest_no>', views.exam, name='exam'),
    path('resault/',views.resault,name='resault'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('exam/',views.exam_redirect,name='exam redirect'),
    path('contact/',views.contact,name="contact")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)