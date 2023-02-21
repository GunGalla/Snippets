from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippet/<int:id>/delete/', views.snippet_delete, name='snippet_delete'),
    path('snippet/<int:id>/', views.snippet, name='dist_snippet'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='snippet_list'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
