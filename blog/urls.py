from django.urls import path, re_path

from .views import (
		BlogDetailView,
		BlogCreateView,
		BlogUpdateView,
	)

urlpatterns = [
	path('b/<slug>/', BlogDetailView.as_view(), name='blog-detail'),
	path('b/<slug>/edit/', BlogUpdateView.as_view(), name='blog-update'),
	path('create/', BlogCreateView.as_view(), name='blog-create'),
]
