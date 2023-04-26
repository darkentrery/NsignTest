from django.urls import path

from nsign.documents import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("create/", views.CreateDocumentView.as_view(), name='create'),
    path("update/<int:pk>/", views.UpdateDocumentView.as_view(), name='update'),
    path("delete/<int:pk>/", views.DeleteDocumentView.as_view(), name='delete'),
]