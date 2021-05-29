from django.urls import path
from . import views

app_name = 'Shop'
urlpatterns = [
    path('category-list/', views.category_list, name='list_category'),
    path('category/', views.create_category, name='create_category'),
    path('update-category/<int:pk>', views.update_category, name='update_category'),
    path('delete-category/<int:pk>', views.delete_category, name='delete_category'),
    path('tag-list/', views.tag_list, name='tag_list'),
    path('tag/', views.create_tag, name='create_tag'),
    path('update-tag/<int:pk>', views.update_tag, name='update_tag'),
    path('delete-tag/<int:pk>', views.delete_tag, name='delete_tag'),
    path('product/', views.create_product, name='create_product'),
    path('update/<int:pk>', views.update_product, name='update_product'),
    path('delete/<int:pk>', views.delete_product, name='delete_product'),
]
