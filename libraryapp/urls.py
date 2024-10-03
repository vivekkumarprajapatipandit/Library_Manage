from django.contrib import admin
from django.urls import include, path
from django.urls import path
from libraryapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('Library', views.Library, name='Library'),
    path('login_entry', views.login_entry, name='login_entry'),
    path('login_submit', views.login_submit, name='login_submit'),
    path('Book_entry', views.Book_entry, name='Book_entry'),
    path('submit', views.submit, name='submit'),
    path('register/', views.register, name='register'),
    path('display', views.display, name='display'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

  