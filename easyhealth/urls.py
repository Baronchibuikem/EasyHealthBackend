"""mambilladb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ==================================
# DJANGO ADMIN custom
# ==================================
admin.site.site_header = "EasyHealth"
admin.site.site_title = "EasyHealth Portal"
admin.site.index_title = "Welcome to EasyHealth Portal"

schema_view = get_schema_view(
    openapi.Info(
        title="EasyHealth API",
        default_version='v1',
        description="A health platform that gears to make access to work class health personnel seamless",
        # terms_of_service="https://www.google.com/policies/terms/",
        #   contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    # This will take you to the admin interface
    # path('admin/', admin.site.urls),
    path('api/v1/', include('account.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # This will show you all the available endpoint in this project
    # path('doc/', schema_view),
    path('swagger(<format>\.json|\.yaml)',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path('accounts/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
