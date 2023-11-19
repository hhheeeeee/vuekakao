from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('duplicateID/<str:username>', views.duplicateID),
]

