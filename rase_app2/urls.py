from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.TableListView.as_view(), name='time_page'),
    path('time-admin/', views.TimeAdminView.as_view(), name='time_admin_page'),
    # path('delete_card/', views.delete_card, name='delete_card'),
     path('delete_card/<int:card_id>/', views.delete_card, name='delete_card'),

]