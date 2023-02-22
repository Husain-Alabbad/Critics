from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    
   

    # CRUD Routes for TV shows
    path('tvshows/', views.ShowList.as_view(), name='tvshows_index'),
    path('tvshows/<int:pk>/', views.ShowDetail.as_view(), name='tvshows_detail'),
    path('tvshows/create/', views.ShowCreate.as_view(), name='tvshows_create'),
    path('tvshows/<int:pk>/update/', views.ShowUpdate.as_view(), name='tvshows_update'),
    path('tvshows/<int:pk>/delete/', views.ShowDelete.as_view(), name='tvshows_delete'),
    path('tvshows/<int:model_id>/<int:category_id>/add_review', views.add_review, name='add_review_tvshow'),


    # # CRUD Routes for novels
    path('novels/', views.NovelList.as_view(), name='novels_index'),
    path('novels/<int:pk>/', views.NovelDetail.as_view(), name='novels_detail'),
    path('novels/create/', views.NovelCreate.as_view(), name='novels_create'),
    path('novels/<int:pk>/update/',
         views.NovelUpdate.as_view(), name='novels_update'),
    path('novels/<int:pk>/delete/',
         views.NovelDelete.as_view(), name='novels_delete'),
    path('novels/<int:model_id>/<int:category_id>/add_review', views.add_review, name='add_review_novel'),

    # # CRUD Routes for games
    path('games/', views.GameList.as_view(), name='games_index'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='games_detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:model_id>/<int:category_id>/add_review', views.add_review, name='add_review_game'),
# /<int:category_id>
    # CRUD Routes for Stars
    path('stars/', views.StarList.as_view(), name='stars_index'),
    path('stars/<int:pk>/', views.StarDetail.as_view(), name='stars_detail'),
    path('stars/create/', views.StarCreate.as_view(), name='stars_create'),
    path('stars/<int:pk>/update/',views.StarUpdate.as_view(), name='stars_update'),
    path('stars/<int:pk>/delete/',views.StarDelete.as_view(), name='stars_delete'),
    path('stars/<int:model_id>/<int:category_id>/add_review', views.add_review, name='add_review_star'),

    # CRUD Routes for directors
    path('directors/', views.DirectorList.as_view(), name='directors_index'),
    path('directors/<int:pk>/', views.DirectorDetail.as_view(),name='directors_detail'),
    path('directors/create/', views.DirectorCreate.as_view(),name='directors_create'),
    path('directors/<int:pk>/update/',views.DirectorUpdate.as_view(), name='directors_update'),
    path('directors/<int:pk>/delete/',views.DirectorDelete.as_view(), name='directors_delete'),
    path('directors/<int:model_id>/<int:category_id>/add_review', views.add_review, name='add_review_director'),
         

    # # CRUD Routes for authors
    path('authors/', views.AuthorList.as_view(), name='authors_index'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(),name='authors_detail'),
    path('authors/create/', views.AuthorCreate.as_view(),name='authors_create'),
    path('authors/<int:pk>/update/',views.AuthorUpdate.as_view(), name='authors_update'),
    path('authors/<int:pk>/delete/',views.AuthorDelete.as_view(), name='authors_delete'),
    path('authors/<int:model_id>/<int:category_id>/add_review', views.add_review, name='add_review_author'),
        # Many to Many
    # Associate a director with a show
    path('shows/<int:show_id>/assoc_toy/<int:director_id>/', views.assoc_director, name="assoc_director"),

    # Unassociate a Director from a Show
    path('shows/<int:show_id>/unassoc_toy/<int:director_id>/', views.unassoc_director, name="unassoc_director"),

]
