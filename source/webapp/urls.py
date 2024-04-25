from django.urls import path
from webapp.views import index, test_list_view, test_detail_view, test_pass_view
app_name: str = 'webapp'

urlpatterns = [
    path('', index, name='index'),
    path('test_list/', test_list_view, name='test_list_view'),
    path('test/<int:test_set_id>/', test_detail_view, name='test_detail_view'),
    path('test/<int:test_set_id>/pass/', test_pass_view, name='test_pass_view'),
]
