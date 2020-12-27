from django.urls import path
from .views import (
    annual_records_m_view,
    annual_records_w_view,
    distances_list_view,
    distance_detail_view,
    events_create_view,
    events_detail_view,
    events_delete_view,
    events_for_year_list_view,
    events_update_view,
    get_years_with_annual_records_m_view,
    get_years_with_annual_records_w_view,
    get_years_with_events_view,
    record_list_m_view,
    record_list_w_view,
    statistics_view
)

# url namespace, if there are several apps
#
app_name = 'resultsapp'

urlpatterns = [
    path('annualrecordlistm', get_years_with_annual_records_m_view, name='annual-record-list-m'),
    path('annualrecordlistm/year:<int:year>/', annual_records_m_view, name='annual-records-m-for-year-list'),
    path('annualrecordlistw', get_years_with_annual_records_w_view, name='annual-record-list-w'),
    path('annualrecordlistw/year:<int:year>/', annual_records_w_view, name='annual-records-w-for-year-list'),
    path('distances', distances_list_view, name='distances-list'),
    path('distances/<int:id>/', distance_detail_view, name='distance-details'),
    path('events', get_years_with_events_view, name='events-list'),
    path('events/year:<int:year>/', events_for_year_list_view, name='events-for-year-list'),
    path('event/create/', events_create_view, name='events-create'),
    path('event/<int:id>/', events_detail_view, name='events-detail'),
    path('event/<int:id>/update/', events_update_view, name='events-update'),
    path('event/<int:id>/delete/', events_delete_view, name='events-delete'),
    path('recordlistm', record_list_m_view, name='record-list-m'),
    path('recordlistw', record_list_w_view, name='record-list-w'),
    path('statistics', statistics_view, name='statistics'),
]
