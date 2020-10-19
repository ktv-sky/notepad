from django.urls import path

from . import views


urlpatterns = [
    path('', views.note_list_view, name='note-list'),
    path('finish-item/<int:id>', views.finish_item, name='finish-note-item'),
    path('delete-item/<int:id>', views.delete_item, name='delete-note-item'),
    path('recover-item/<int:id>', views.recover_item, name='recover-note-item'),
]
