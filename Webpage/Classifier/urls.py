from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('predict', views.predict_sentence, name='predict'),
    path('upload', views.upload, name='upload'), #TODO: Potentially not needed if not uploading train/test data
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #TODO: Same as at upload