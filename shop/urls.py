from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$", views.index, name="ShopHome"),
    url(r"^about/", views.about, name="AboutUs"),
    url(r"^contact/", views.contact, name="ContactUs"),
    url(r"^tracker/", views.tracker, name="TrackingStatus"),
    url(r"^search/", views.search, name="Search"),
    url(r"^products/(\d+)/", views.productView, name="ProductView"),
    url(r"^checkout1/(\d+)/", views.checkout2, name="Checkout"),
    url(r"^checkout/(\d+)", views.checkout, name="Checkout"),
    url(r"^handlerequest/", views.handlerequest, name="HandleRequest"),
]