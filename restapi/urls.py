from django.urls import path, include

urlpatterns = [
    path(r'v1/', include(('restapi.v1.urls', 'v1'), namespace='v1')),
]
