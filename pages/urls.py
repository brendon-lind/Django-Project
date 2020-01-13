from django.urls import path, include


from .views import HomeView, AboutView


urlpatterns = [
    path('', HomeView.as_view()),
    path('about', AboutView.as_view()),
]
