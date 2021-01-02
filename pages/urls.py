from django.urls import path
from cadastros.views import WalletView
from . import views
app_name = "pages"

urlpatterns = [
    path("", WalletView.as_view(), name="home"),
]