from django.urls import path
from .views import TestAppView, get_users


urlpatterns = [
    path(
        route='cbv/',
        view=TestAppView.as_view(),
        name='test_app'
    ),
    path(
        route='fbv/',
        view=get_users,
        name='test_app'
    )
]
