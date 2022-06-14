from django.urls import path, include

from rest_framework.permissions import AllowAny
from rest_framework.schemas import get_schema_view

from accounts.api import views as account_views
from profiles.api import views as profile_views
from games.api import views as game_views
from sales.api import views as sale_views
from test_app.api import views as test_views


urlpatterns = [
    # {% url 'api:games' %}
    path(
        route='games/',
        view=game_views.GameListAPIView.as_view(),
        name='games'
    ),
    # {% url 'api:games' game.uuid %}
    path(
        route='games/<uuid:uuid>/',
        view=game_views.GameDetailAPIView.as_view(),
        name='games'
    ),
    # {% url 'api:games' %}
    path(
        route='games/ratings/',
        view=game_views.RatingListCreateAPIView.as_view(),
        name='games_ratings'
    ),


    # {% url 'api:Sales' %}
    path(
        route='sales/',
        view=sale_views.SaleListAPIView.as_view(),
        name='sales'
    ),
    # {% url 'api:Sales' sale.uuid %}
    path(
        route='sales/<uuid:uuid>/',
        view=sale_views.SaleDetailAPIView.as_view(),
        name='sales'
    ),

    # Auth
    path(
        route='auth/',
        view=include('drf_social_oauth2.urls', namespace='drf'),
        name='auth'
    ),
    path(
        route='auth/signup/',
        view=account_views.UserSignUpAPIView.as_view(),
        name='auth'
    ),
    path(
        route='auth/confirm-email/',
        view=account_views.UserConfirmEmailAPIView.as_view(),
        name='auth'
    ),

    # Profile
    path(
        route='profile/',
        view =profile_views.ProfileDetailAPIView.as_view(),
        name='profile'
    ),

    # For Testing
    path(
        route='test_image/create/',
        view=test_views.TestCreateAPIView.as_view(),
        name='test_app'
    ),
    # ----------

    path(
        route='schema/',
        view=get_schema_view(
            permission_classes=[AllowAny],
            title='GamesSalesAPI',
            description='API for the GamesSalesAPI',
            version='1.0.0'
        ),
        name='openapi-schema'
    ),
]
