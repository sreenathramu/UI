from django.conf.urls import url
import views

urlpatterns = [
    url(r'^distribution/',views.genderDistribution),
    url(r'^rows/',views.getAlldata),
    url(r'^relationship/',views.getRelationshipCount)
]