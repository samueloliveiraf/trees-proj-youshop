from django.urls import path


urlpatterns = [
    path("", views.TreesView.as_view(), name="trees"),
]
