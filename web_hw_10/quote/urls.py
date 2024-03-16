from django.urls import path
from . import views

app_name = 'quote'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
    path('author/', views.author, name='author'),
    path(
        'detail_author/<int:author_id>',
        views.author_detail,
        name='author_detail'
    ),
    path(
        'done_author/<int:author_id>',
        views.set_done_author,
        name='author_set_done'
    ),
    path(
        'delete_author/<int:author_id>',
        views.delete_author,
        name='author_delete'
    ),
    path('quote/', views.quote, name='quote'),
    path('detail/<int:quote_id>', views.detail, name='detail'),
    path('done/<int:quote_id>', views.set_done, name='set_done'),
    path('delete/<int:quote_id>', views.delete_quote, name='delete'),
]
