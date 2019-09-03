from django.urls import path

from restaurants.views import UploadFileView


urlpatterns = [
    path('upload_restaurants/', UploadFileView.as_view(), name='upload-restaurants'),
]
