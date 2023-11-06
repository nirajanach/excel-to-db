
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

admin.site.site_header = 'Goondir Health Services'
admin.site.index_title = 'Goondir'
admin.site.site_title = 'Goondir Health Services'
urlpatterns = [
    path('admin/', admin.site.urls),

    path('goondir/', include('django.contrib.auth.urls')),


    path('goondir/', include('goondirApp.urls'))
]
