from django.urls import path

from test_app.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]

