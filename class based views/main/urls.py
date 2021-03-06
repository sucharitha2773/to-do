from django.urls import path
from main import views

urlpatterns = [
    path('stylelist/', views.StyleList.as_view(), name= 'stylelist'),
    path('createstyle/',views.CreateStyle.as_view(),name='createstyle'),
    path('style/<int:pk>/delete/',views.StyleDelete.as_view(),name='styledelete'),
    path('style/<int:pk>/detail/',views.StyleDetail.as_view(),name='styledetail'),
    path('style/<int:pk>/update/',views.StyleUpdate.as_view(),name='styleupdate'),


]