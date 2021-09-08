from django.urls import path
from FA import views

urlpatterns = [
    path('list/', views.article_list),
    path('detail/', views.article_detail),
]
