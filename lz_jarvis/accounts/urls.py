from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf.urls import url, include

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
]