from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from zoo_backend import settings

from core.swagger.view import schema_view

# from zoo.api.v1.urls import router

from zoo.api.v1.views.workers import WorkersDetailsView, WorkersListView
from zoo.api.v1.views.faq import FAQListView, FAQDetailsView
from zoo.api.v1.views.country import CountryListView, CountryDetailsView
from zoo.api.v1.views.category import CategoryListView, CategoryDetailsView
from zoo.api.v1.views.animal import AnimalDetailsView, AnimalListView
from zoo.api.v1.views.about import AboutDetailsView, AboutListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/workers/', WorkersListView.as_view()),
    path('api/v1/workers/<int:pk>/', WorkersDetailsView.as_view()),
    path('api/v1/faq/', FAQListView.as_view()),
    path('api/v1/faq/<int:pk>/', FAQDetailsView.as_view()),
    path('api/v1/country/', CountryListView.as_view()),
    path('api/v1/country/<int:pk>/', CountryDetailsView.as_view()),
    path('api/v1/category/', CategoryListView.as_view()),
    path('api/v1/category/<int:pk>/', CategoryDetailsView.as_view()),
    path('api/v1/animal/', AnimalListView.as_view()),
    path('api/v1/animal/<int:pk>/', AnimalDetailsView.as_view()),
    path('api/v1/about/', AboutListView.as_view()),
    path('api/v1/about/<int:pk>/', AboutDetailsView.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
                static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
if settings.USE_SWAGGER:
    urlpatterns.extend((
        re_path(r'api/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path(r'api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path(r'api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ))

admin.site.site_header = 'Zoo Admin Panel'
admin.site.site_title = 'Zoo'
