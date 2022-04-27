from django.urls import path, include
from rest_framework.authtoken import views
from .views import CreateUserView, UserView

urlpatterns = [
    path('register/', CreateUserView.as_view()),
    path('', include('rest_framework.urls')), # login/, logout/
    path('obtain-token/', views.obtain_auth_token),
    path('account/<int:id>',UserView.as_view())
]
