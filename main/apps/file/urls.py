from django.urls import path
from . import views


urlpatterns = [
    path(
        'file-create/', 
        views.file_list_create_api_view, 
        name='file_list_create'
    ),
    path(
        'file/<int:id>/', 
        views.file_api_view, 
        name='file_update_delete'
    ),
    path(
        'file-share/<int:id>/', 
        views.file_share_api_view, 
        name='file_share'
    ),
    path(
        'filegroup-create/', 
        views.filegroup_list_create_api_view, 
        name='filegroup_list_create'
    ),
    path(
        'filegroup/<int:id>/', 
        views.filegroup_api_view, 
        name='filegroup_update_delete'
    )
]