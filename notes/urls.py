"""
notes/urls.py
"""
from django.urls import path
from .views import (
    all_notes,
    view_note,
    write_note,
    edit_note,
    delete_note
)

urlpatterns = [
    path("", all_notes, name="all_notes"),
    path("note/<int:pk>/", view_note, name="view_note"),
    path("note/new/", write_note, name="write_note"),
    path("note/<int:pk>/edit/", edit_note, name="edit_note"),
    path("note/<int:pk>/delete/", delete_note, name="delete_note"),
]