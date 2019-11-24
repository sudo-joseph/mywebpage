from django.urls import path

import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.index,name='index'),
    path('index', views.index),
    path('projects', views.projects,name='projects'),
    path('contact', views.contact,name='contact'),
    path('blog/<slug:title>', views.post, {'root':'index'}, name='blog',),
    path('projects/<slug:title>', views.post, {'root':'projects'}, name='projects',),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
