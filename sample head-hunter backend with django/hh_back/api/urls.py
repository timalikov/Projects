from django.urls import path
from . import views


urlpatterns = [
    path('companies/', views.companies, name="get all companies"),
    path('companies/<int:company_id>/', views.get_company_by_id, name="get company by id"),
    path('companies/<int:company_id>/vacancies/', views.company_vacancies, name="get company vacancies"),
    path('vacancies/', views.vacancies, name="get all vacancies"),
    path('vacancies/<int:vacancy_id>/', views.get_vacancy_by_id, name="get vacancy by id"),
    path('vacancies/top_ten', views.get_top_ten_vacancies),

    # path('products/<int:product_id>/', views.product_detail, name="get product"),
    # path('categories/', views.get_categories, name="get all categories"),
    # path('categories/<int:category_id>/', views.get_category, name="get category"),
    # path('categories/<int:category_id>/products/', views.get_category_products, name="get category products"),
]