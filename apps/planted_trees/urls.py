from django.urls import path
from .views import (
    success_page,
    plant_tree,
    user_planted_trees,
    user_planted_trees_admin,
    api_user_planted_trees
)

urlpatterns = [
    path('plant-tree/', plant_tree, name='plant_tree'),
    path('user-planted-trees/', user_planted_trees, name='user_planted_trees'),
    path('user-planted-trees-admin/', user_planted_trees_admin, name='user_planted_trees_admin'),
    path('success/', success_page, name='success_page'),
    # API User Planted Trees
    path('api-user-planted-trees/<str:user_id>/', api_user_planted_trees, name='api_user_planted_trees')
]
