from django.urls import path, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="test_app/home.html"), name='home'),
    re_path(r"^(/([A-Za-z0-9])*)*", TemplateView.as_view(template_name="test_app/some_page.html"))
]

