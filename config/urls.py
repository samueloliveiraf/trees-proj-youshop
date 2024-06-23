from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include
from django.contrib import admin

from apps.planted_trees import urls as urls_planted_trees
from apps.accounts import urls as urls_accounts

from apps.core.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(urls_accounts)),
    path('trees/', include(urls_planted_trees)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', home, name='home')
]
