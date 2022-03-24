from django.urls import path
from .import views
from .views import AddPostView, IndexView , ArticleView,UpdatePostView


urlpatterns = [
    #path('',views.index)
    path('',IndexView.as_view(),name='index'),
    path('article/<int:pk>',ArticleView.as_view(),name='article-detail'),
    path('addpost/', AddPostView.as_view(),name='addpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(),name='updatepost')
]