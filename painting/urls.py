from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.upload_painting, name='upload'),
    path('', views.painting_list,name='list'),
    path('detail/<int:pk>/',views.painting_detail,name='detail'),
    path('detail/<int:pk>/like',views.like_painting,name='detailLike'),
    path('detail/<int:pk>/unlike',views.unlike_painting,name='detailUnlike'),
    path('search/',views.painting_search,name='search')
]
