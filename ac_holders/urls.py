from django.urls import path

from .views import AccountViews

urlpatterns = [
    path('manage', AccountViews.as_view(), name='account'),
]
