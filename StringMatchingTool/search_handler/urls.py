from django.urls import path, re_path
from . import views

urlpatterns = [
    path('upload/', views.upload_files, name='upload_files'),
    path('results/<str:results_id>/<str:query>/', views.get_results, name='get_results'),
]
