from django.urls import path
from . import views
urlpatterns = [
    path('', views.painting_list,name='list'),
    path('create/', views.create_painting, name='create'),
    path('<int:pk>/',views.painting_detail,name='detail'),
    path('<int:pk>/update', views.update_painting, name='update'),
    path('<int:pk>/like',views.like_painting,name='detailLike'),
    path('<int:pk>/unlike',views.unlike_painting,name='detailUnlike'),
    path('<int:pk>/delete',views.delete_painting,name='delete'),
    path('search/',views.painting_search,name='search')
]
