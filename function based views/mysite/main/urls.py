from django.urls import path
from main.views import post_list,post_new,post_delete,post_detail,post_update

urlpatterns = [
    path('',post_list,name= 'postlist'),
    path('postnew/',post_new, name='postnew'),
    path('post/<int:pk>/detail/',post_detail,name='postdetail'),
    path('post/<int:pk>/delete/',post_delete, name='postdelete'),
    path('post/<int:pk>/edit/',post_update,name='postupdate'),


]