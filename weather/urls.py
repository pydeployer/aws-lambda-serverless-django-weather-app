"""
URL configuration for weather project.

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
from django.urls import path
from weather.portal import views
from weather.articles import views as articles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('weather/<str:city>/', views.city_weather, name='city_weather'),

    # articles
    path('conditions/temperature/', articles_views.temperature_article, name='temperature_article'),
    path('conditions/precipitation/', articles_views.precipitation_article, name='precipitation_article'),
    path('conditions/wind/', articles_views.wind_article, name='wind_article'),
    path('conditions/uv-index/', articles_views.uv_article, name='uv_article'),
]
