from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.AutoListView.as_view()),
    path('autos', views.AutoListView.as_view(), name='autos'),
    path('autos/<int:pk>', views.AutoDetailView.as_view(), name='auto_detail'),
    path('autos/create',
        views.AutoCreateView.as_view(success_url=reverse_lazy('autos')), name='auto_create'),
    path('auto/<int:pk>/update',
        views.AutoUpdateView.as_view(success_url=reverse_lazy('autos')), name='auto_update'),
    path('auto/<int:pk>/delete',
        views.AutoDeleteView.as_view(success_url=reverse_lazy('autos')), name='auto_delete'),
    path('auto/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('autos')), name='comment_delete'),
]
